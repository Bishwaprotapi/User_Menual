"""Generate a user manual from screenshots using the prompt in PROMPT_TEMPLATE.md."""
import argparse
from pathlib import Path

from google import genai
from google.genai import types
from PIL import Image

HERE = Path(__file__).parent
ROOT = HERE.parent
SCREENSHOTS_DIR = ROOT / "screenshots"
PROMPT_TEMPLATE = ROOT / "config" / "PROMPT_TEMPLATE.md"
MODEL = "gemini-2.0-flash"  # free tier


def build_prompt(software_name: str, core_purpose: str, audience: str) -> str:
    text = PROMPT_TEMPLATE.read_text(encoding="utf-8")
    text = text.replace("[Software Name, e.g., TaskFlow Pro]", software_name)
    text = text.replace("[Core Purpose, e.g., Project Management and Task Tracking]", core_purpose)
    text = text.replace("[Audience, e.g., Non-technical team members and managers]", audience)
    return text


def load_screenshots() -> list[Image.Image]:
    images = [Image.open(p) for p in sorted(SCREENSHOTS_DIR.iterdir()) if p.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp")]
    if not images:
        raise SystemExit(f"No screenshots found in {SCREENSHOTS_DIR} — add image files first.")
    return images


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--name", required=True, help="Software name, e.g. TaskFlow Pro")
    parser.add_argument("--purpose", required=True, help="Core purpose, e.g. Project Management")
    parser.add_argument("--audience", required=True, help="Target audience, e.g. Non-technical managers")
    parser.add_argument("--output", default=str(ROOT / "manual.md"), help="Output path for the generated manual")
    args = parser.parse_args()

    prompt = build_prompt(args.name, args.purpose, args.audience)
    images = load_screenshots()

    client = genai.Client()  # reads GEMINI_API_KEY / GOOGLE_API_KEY from env
    response = client.models.generate_content(
        model=MODEL,
        contents=[*images, prompt],
        config=types.GenerateContentConfig(max_output_tokens=8192),
    )

    Path(args.output).write_text(response.text, encoding="utf-8")
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
