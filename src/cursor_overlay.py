"""Inject a synthetic mouse cursor + highlight ring into a page before a screenshot.

Headless Chromium screenshots never contain the real OS cursor, so every
capture in this pipeline draws a fake one at the coordinates of whatever was
just clicked (or is about to be clicked). The overlay is absolutely
positioned in document coordinates (viewport point + current scroll offset)
so it stays pinned to the right spot even when Playwright's full-page
screenshot temporarily resizes the viewport to the page's full height.
"""

CURSOR_SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" '
    'viewBox="0 0 24 24">'
    '<path d="M3 2 L3 19 L7.5 15.6 L10.2 21.4 L13.1 20 L10.4 14.3 L16 14 Z" '
    'fill="#111" stroke="#fff" stroke-width="1.3" stroke-linejoin="round"/>'
    "</svg>"
)

_MARKER_ID = "__manual_cursor_overlay__"

_SHOW_SCRIPT = """([x, y, svg, markerId]) => {
    const old = document.getElementById(markerId);
    if (old) old.remove();

    const scrollX = window.scrollX || document.documentElement.scrollLeft || 0;
    const scrollY = window.scrollY || document.documentElement.scrollTop || 0;

    const ring = document.createElement('div');
    ring.id = markerId;
    ring.style.cssText = `
        position: absolute;
        left: ${x + scrollX - 20}px;
        top: ${y + scrollY - 20}px;
        width: 40px;
        height: 40px;
        border-radius: 50%;
        border: 3px solid #ff3b30;
        background: rgba(255, 59, 48, 0.18);
        box-shadow: 0 0 0 4px rgba(255, 59, 48, 0.25);
        z-index: 2147483647;
        pointer-events: none;
    `;

    const cursor = document.createElement('div');
    cursor.style.cssText = `
        position: absolute;
        left: 12px;
        top: 12px;
        width: 26px;
        height: 26px;
        filter: drop-shadow(0 1px 2px rgba(0,0,0,0.6));
    `;
    cursor.innerHTML = svg;

    ring.appendChild(cursor);
    document.body.appendChild(ring);
}"""

_HIDE_SCRIPT = """(markerId) => {
    const old = document.getElementById(markerId);
    if (old) old.remove();
}"""


def show(page, x: float, y: float) -> None:
    """Draw the cursor + highlight ring centered at viewport point (x, y)."""
    try:
        page.evaluate(_SHOW_SCRIPT, [x, y, CURSOR_SVG, _MARKER_ID])
    except Exception:
        pass


def hide(page) -> None:
    try:
        page.evaluate(_HIDE_SCRIPT, _MARKER_ID)
    except Exception:
        pass


def locator_center(locator) -> tuple[float, float] | None:
    """Best-effort viewport center point of a Playwright locator, or None."""
    try:
        box = locator.bounding_box(timeout=1500)
    except Exception:
        return None

    if not box:
        return None

    return (box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)


def default_point(page) -> tuple[float, float]:
    """A reasonable fallback point when no specific element is known."""
    try:
        viewport = page.viewport_size or {"width": 1920, "height": 1000}
    except Exception:
        viewport = {"width": 1920, "height": 1000}

    return (viewport["width"] / 2, 60)
