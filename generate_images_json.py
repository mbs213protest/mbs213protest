#!/usr/bin/env python3
"""
generate_images_json.py
/images/ フォルダ内の jpg/png を走査して images.json を生成します。
GitHub Pages にデプロイする前に実行してください。

使い方:
  python generate_images_json.py

実行するとこのスクリプトと同じ階層に images.json が生成されます。
"""
import json
import os
from pathlib import Path

IMAGES_DIR = Path(__file__).parent / "images"
OUTPUT     = Path(__file__).parent / "images.json"
EXTS       = {".jpg", ".jpeg", ".png"}

def main():
    if not IMAGES_DIR.exists():
        print(f"[!] images/ フォルダが見つかりません: {IMAGES_DIR}")
        return

    files = sorted(
        f"images/{p.name}"
        for p in IMAGES_DIR.iterdir()
        if p.is_file() and p.suffix.lower() in EXTS
    )

    if not files:
        print("[!] images/ フォルダに jpg/png ファイルがありません。")
    else:
        print(f"[+] {len(files)} 件の画像を検出:")
        for f in files:
            print(f"    {f}")

    OUTPUT.write_text(json.dumps(files, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n[✓] {OUTPUT} を生成しました。")

if __name__ == "__main__":
    main()
