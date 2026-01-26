import os
from pathlib import Path

from storage import upload_to_r2


def main():
    base_dir = Path(__file__).resolve().parents[1]
    guide_dir = base_dir / "static" / "videos" / "3DexerciseVIdeo"

    if not guide_dir.exists():
        raise FileNotFoundError(f"Guide video folder not found: {guide_dir}")

    uploaded = 0
    for file_path in guide_dir.glob("*.mp4"):
        key = f"videos/3DexerciseVideo/{file_path.name}"
        url = upload_to_r2(str(file_path), key, delete_local=False)
        if url:
            uploaded += 1
            print(f"Uploaded: {file_path.name} -> {url}")
        else:
            print(f"Failed: {file_path.name}")

    print(f"Done. Uploaded {uploaded} files.")


if __name__ == "__main__":
    main()
