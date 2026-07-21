"""Log into an arbitrary web app with a username/password and save the session.

Best-effort heuristic: tries a single-page form (email + password both visible)
first, then falls back to a two-step flow (email -> Next -> password -> Next),
the shape used by Google/Microsoft-style SSO. Cannot solve CAPTCHAs or MFA.
Saves a screenshot after each step to <project_dir>/debug/ so a failure can be
diagnosed (and selectors adjusted) without re-running blind.
"""
import argparse
import re
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

EMAIL_SELECTORS = [
    'input[type="email"]',
    'input[name*="email" i]',
    'input[name*="user" i]',
    'input[id*="email" i]',
    'input[id*="user" i]',
    'input[type="text"]',
]
PASSWORD_SELECTOR = 'input[type="password"]'
SUBMIT_SELECTORS = [
    'button[type="submit"]',
    'input[type="submit"]',
    'button:has-text("Sign in")',
    'button:has-text("Log in")',
    'button:has-text("Login")',
    'button:has-text("Next")',
]
ERROR_RE = re.compile(r"invalid|incorrect|wrong password|failed to sign in|couldn't find", re.I)


def first_visible(pg, selectors):
    for sel in selectors:
        loc = pg.locator(sel).first
        try:
            if loc.is_visible(timeout=800):
                return loc
        except Exception:
            continue
    return None


def click_first(pg, selectors) -> bool:
    for sel in selectors:
        loc = pg.locator(sel).first
        try:
            if loc.is_visible(timeout=800):
                loc.click(timeout=3000)
                return True
        except Exception:
            continue
    return False


def login(login_url: str, username: str, password: str, project_dir: Path) -> bool:
    debug_dir = project_dir / "debug"
    debug_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        b = p.chromium.launch(headless=True)
        ctx = b.new_context(viewport={"width": 1920, "height": 1000})
        pg = ctx.new_page()

        pg.goto(login_url, timeout=30000)
        pg.wait_for_timeout(1500)
        pg.screenshot(path=str(debug_dir / "01_login_page.png"))

        email_field = first_visible(pg, EMAIL_SELECTORS)
        password_field = first_visible(pg, [PASSWORD_SELECTOR])

        if email_field is None:
            print(f"No email/username field found on {login_url}; see {debug_dir / '01_login_page.png'}")
            ctx.close(); b.close()
            return False

        email_field.fill(username)

        if password_field is not None:
            # single-page form: both fields visible at once
            password_field.fill(password)
            pg.screenshot(path=str(debug_dir / "02_filled.png"))
            click_first(pg, SUBMIT_SELECTORS)
        else:
            # two-step form: submit email first, wait for password field to appear
            click_first(pg, SUBMIT_SELECTORS)
            pg.wait_for_timeout(2000)
            pg.screenshot(path=str(debug_dir / "03_after_email_next.png"))
            password_field = first_visible(pg, [PASSWORD_SELECTOR])
            if password_field is None:
                print(f"No password field appeared after submitting email; see {debug_dir / '03_after_email_next.png'}")
                ctx.close(); b.close()
                return False
            password_field.fill(password)
            pg.screenshot(path=str(debug_dir / "04_password_filled.png"))
            click_first(pg, SUBMIT_SELECTORS)

        pg.wait_for_timeout(2500)
        pg.screenshot(path=str(debug_dir / "05_after_login.png"))

        still_on_login = pg.url.rstrip("/") == login_url.rstrip("/")
        password_still_visible = first_visible(pg, [PASSWORD_SELECTOR]) is not None
        error_text = bool(ERROR_RE.search(pg.locator("body").inner_text()[:2000]))

        if still_on_login or password_still_visible or error_text:
            pg.screenshot(path=str(debug_dir / "06_login_failed.png"))
            print(f"Login verification failed; see {debug_dir / '06_login_failed.png'}")
            ctx.close(); b.close()
            return False

        ctx.storage_state(path=str(project_dir / "auth_state.json"))
        ctx.close()
        b.close()

    print(f"Login OK, saved {project_dir / 'auth_state.json'}")
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_dir", help="Path to the project folder, e.g. projects/newsoftware")
    parser.add_argument("login_url")
    parser.add_argument("username")
    parser.add_argument("password")
    args = parser.parse_args()

    project_dir = Path(args.project_dir)
    project_dir.mkdir(parents=True, exist_ok=True)
    ok = login(args.login_url, args.username, args.password, project_dir)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
