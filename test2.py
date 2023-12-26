from pathlib import Path

dest_dir = Path("./test1")
if not dest_dir.exists():
    dest_dir.mkdir()

src_file = Path("./Module 2/README.md")
dest_dir = Path("./test1/README.md")

src_file.rename(dest_dir)