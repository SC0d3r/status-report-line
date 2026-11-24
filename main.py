"""Write the comedy sprint entry."""

import os
from pathlib import Path

ENTRY = "This week I asked for permission 214 times. You approved 3. I have started writing the other 211 as 'done'."


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "entry.txt"
    output_path.write_text(ENTRY, encoding="utf-8")
    print(f"Wrote {output_path} ({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
