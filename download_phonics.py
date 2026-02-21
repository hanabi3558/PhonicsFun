"""
Phonics 音檔批次下載腳本
使用 Google Translate TTS 下載所有 phonics 發音 mp3

使用方式：
  python download_phonics.py

音檔會存到 ./sounds/ 資料夾
"""

import os
import time
import urllib.request

# 輸出資料夾
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sounds")

# phonicsText 對應表：key = 檔名, value = 要唸的文字
phonics = {
    # === Short vowels ===
    "a": "ah",
    "e": "eh",
    "i": "ill",
    "o": "oh",
    "u": "uh",

    # === Consonants ===
    "b": "buh",
    "c": "kuh",
    "d": "duh",
    "f": "fuh",
    "g": "guh",
    "h": "huh",
    "j": "juh",
    "k": "kuh",
    "l": "luh",
    "m": "muh",
    "n": "nuh",
    "p": "puh",
    "q": "quick",
    "r": "ruh",
    "s": "suh",
    "t": "tuh",
    "v": "vuh",
    "w": "wuh",
    "x": "ex",
    "y": "yuh",
    "z": "zei",

    # === Phase 2: Double letters ===
    "ck": "kuh",
    "ff": "fuh",
    "ll": "luh",
    "ss": "suh",

    # === Phase 3: Consonant digraphs ===
    "ch": "chuh",
    "sh": "shuh",
    "th": "thuh",
    "ng": "ung",
    "qu": "quuh",
    "zz": "zei",

    # === Phase 3: Vowel digraphs & r-controlled vowels ===
    "ai": "ay",
    "ee": "ee",
    "igh": "eye",
    "oa": "oh",
    "oi": "oy",
    "oo": "oo",
    "oo_long": "oo",
    "oo_short": "oo",
    "ar": "ar",
    "or": "or",
    "ur": "er",
    "ow": "ow",
    "ear": "ear",
    "air": "air",
    "ure": "er",
    "er": "er",

    # === Phase 4: Consonant clusters (initial) ===
    "tr": "truh",
    "dr": "druh",
    "gr": "gruh",
    "cr": "cruh",
    "br": "bruh",
    "fr": "fruh",
    "bl": "bluh",
    "fl": "fluh",
    "gl": "gluh",
    "pl": "pluh",
    "cl": "cluh",
    "sl": "sluh",
    "sp": "sper",
    "tw": "twuh",
    "sm": "smur",
    "pr": "pruh",
    "sc": "skuh",
    "sn": "sner",
    "st": "stuh",
    "sw": "swuh",
    "dw": "dwuh",
    "scr": "scruh",
    "shr": "shruh",
    "thr": "thruh",
    "str": "struh",

    # Phase 4: Consonant clusters (final)
    "nd": "und",
    "mp": "ump",
    "nt": "unt",
    "nk": "ink",
    "ft": "oft",
    "sk": "usk",
    "lt": "ult",
    "lp": "elp",
    "lf": "ulf",
    "lk": "ilk",
    "pt": "upt",
    "xt": "ext",
    "nch": "ench",

    # === Phase 5: Advanced vowel sounds ===
    "ay": "ay",
    "ou": "ow",
    "ie": "eye",
    "ea": "ee",
    "oy": "oy",
    "ir": "er",
    "ue": "oo",
    "aw": "aw",
    "wh": "wuh",
    "ph": "fuh",
    "ew": "oo",
    "oe": "oh",
    "au": "aw",
    "ey": "ee",
    "a_e": "ay",
    "e_e": "ee",
    "i_e": "eye",
    "o_e": "oh",
    "u_e": "you",

    # === Phase 6: Tricky patterns ===
    "dge": "gee",
    "ge": "juh",
    "gn": "nuh",
    "kn": "nuh",
    "wr": "ruh",
    "le": "ul",
    "eer": "ear",
    "ture": "chuur",
    "mb": "muh",
    "al": "awl",
    "war": "wor",
    "wor": "wo",
    "wa": "wah",
    "qua": "kwah",
    "tion": "shun",
    "tch": "chuh",

    # === Alternates ===
    "y_as_ee_eye": "eye",
    "a_as_o": "ah",
    "o_as_u": "uh",
    "ey_as_ee": "ee",
    "s_as_zh": "sher",
}


def download_sound(filename, text):
    """用 Google Translate TTS 下載一個音檔"""
    url = (
        f"https://translate.google.com/translate_tts"
        f"?ie=UTF-8&tl=en&client=tw-ob&q={urllib.request.quote(text)}"
    )

    filepath = os.path.join(OUTPUT_DIR, f"{filename}.mp3")

    # 如果已存在就跳過
    if os.path.exists(filepath):
        print(f"  [跳過] {filename}.mp3 (已存在)")
        return True

    try:
        req = urllib.request.Request(url)
        req.add_header("User-Agent", "Mozilla/5.0")
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read()
            with open(filepath, "wb") as f:
                f.write(data)
        print(f"  [OK]  {filename}.mp3  ({len(data)} bytes)")
        return True
    except Exception as e:
        print(f"  [失敗] {filename}.mp3 - {e}")
        return False


def main():
    # 建立輸出資料夾
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    total = len(phonics)
    success = 0
    failed = 0

    print(f"開始下載 {total} 個 phonics 音檔到 {OUTPUT_DIR}\n")

    for i, (filename, text) in enumerate(phonics.items(), 1):
        print(f"[{i}/{total}] {filename} -> \"{text}\"")
        if download_sound(filename, text):
            success += 1
        else:
            failed += 1

        # 每個間隔 0.5 秒，避免被 Google 限流
        if i < total:
            time.sleep(0.5)

    print(f"\n完成！成功: {success}, 失敗: {failed}")
    print(f"音檔位置: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
