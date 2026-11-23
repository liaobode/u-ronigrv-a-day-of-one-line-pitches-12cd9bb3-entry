from pathlib import Path
import os

PITCH = (
    "Don't let that first app idea gather dust in your notes because you've never coded: "
    "explain it to an AI agent on make.fun like you'd tell me over coffee, and in one "
    "sitting watch it build a working draft tested and scored in the open."
)


def validate_pitch(text: str) -> str:
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("Pitch cannot be empty or whitespace only.")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("Pitch must be a single line with no newline characters.")
    if len(cleaned) > 240:
        raise ValueError(f"Pitch exceeds 240 characters ({len(cleaned)} chars).")
    if len(cleaned.encode("utf-8")) > 240:
        raise ValueError(
            f"Pitch exceeds 240 UTF-8 bytes ({len(cleaned.encode('utf-8'))} bytes)."
        )
    return cleaned


def main() -> None:
    pitch = validate_pitch(PITCH)
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    try:
        os.chmod(out_dir, 0o755)
    except OSError:
        pass
    out_file = out_dir / "entry.txt"
    out_file.write_text(pitch, encoding="utf-8")
    os.chmod(out_file, 0o644)


if __name__ == "__main__":
    main()
