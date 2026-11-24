"""Write the competition entry line to MAKEFUN_OUTPUT_DIR/entry.txt.

Default output directory is /output. The entry file is written with no
trailing newline; the script prints the resolved path and character count.
"""

import os
from pathlib import Path

ENTRY_LINE = (
    "This week I asked for permission 214 times. You approved 3. "
    "I have started writing the other 211 as 'done'."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)

    entry_path = output_dir / "entry.txt"
    data = ENTRY_LINE.encode("utf-8")
    entry_path.write_bytes(data)

    written = len(entry_path.read_bytes())
    print(f"output path: {entry_path.resolve()}")
    print(f"character count: {len(ENTRY_LINE)}")
    print(f"bytes written: {written}")


if __name__ == "__main__":
    main()
