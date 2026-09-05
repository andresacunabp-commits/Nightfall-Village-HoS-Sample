import base64
import io
import os
import zipfile

import cv2
import numpy as np

PARTS = [
    "part00.txt", "part01.txt", "part02.txt",
    "part03a.txt", "part03b.txt",
    "part04a.txt", "part04b1.txt", "part04b2.txt",
    "part05a.txt", "part05b.txt",
    "part06a.txt", "part06b.txt",
    "part07a.txt", "part07b.txt",
]

FILES = [
    "village_square.jpg",
    "market_alley.jpg",
    "training_ground.jpg",
    "riverside.jpg",
    "shrine_path.jpg",
    "aya_house_ext.jpg",
    "aya_house_hallway.jpg",
]

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PARTS_DIR = os.path.join(ROOT, "game", "assets", "v10_parts")
OUT_DIR = os.path.join(ROOT, "game", "images", "backgrounds", "v104")
MODEL = os.path.join(ROOT, "tools", "EDSR_x4.pb")


def reconstruct_archive():
    encoded = []
    for name in PARTS:
        path = os.path.join(PARTS_DIR, name)
        if not os.path.isfile(path):
            raise RuntimeError(f"Missing source chunk: {name}")
        with open(path, "r", encoding="ascii") as f:
            encoded.append(f.read().strip())
    raw = base64.b64decode("".join(encoded))
    if raw[:4] != b"PK\x03\x04":
        raise RuntimeError("Rebuilt source art is not a ZIP archive")
    return zipfile.ZipFile(io.BytesIO(raw), "r")


def restore_detail(image):
    # Mild local contrast and edge restoration after EDSR. This is deliberately
    # stronger than the v0.10.3 pass, but avoids obvious halos around lanterns.
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=1.55, tileGridSize=(10, 10))
    l = clahe.apply(l)
    image = cv2.cvtColor(cv2.merge((l, a, b)), cv2.COLOR_LAB2BGR)

    blur = cv2.GaussianBlur(image, (0, 0), 1.05)
    image = cv2.addWeighted(image, 1.34, blur, -0.34, 0)

    # A tiny edge boost makes architecture read better at 1280x720.
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Laplacian(gray, cv2.CV_16S, ksize=3)
    edges = cv2.convertScaleAbs(edges)
    edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    image = cv2.addWeighted(image, 1.0, edges, 0.055, 0)
    return image


def main():
    if not os.path.isfile(MODEL):
        raise RuntimeError("EDSR model is missing")

    os.makedirs(OUT_DIR, exist_ok=True)

    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    sr.readModel(MODEL)
    sr.setModel("edsr", 4)

    archive = reconstruct_archive()

    for name in FILES:
        data = archive.read(name)
        source = cv2.imdecode(np.frombuffer(data, np.uint8), cv2.IMREAD_COLOR)
        if source is None:
            raise RuntimeError(f"Could not decode {name}")

        enlarged = sr.upsample(source)
        native = cv2.resize(enlarged, (1280, 720), interpolation=cv2.INTER_LANCZOS4)
        native = restore_detail(native)

        out = os.path.join(OUT_DIR, name)
        ok = cv2.imwrite(out, native, [
            int(cv2.IMWRITE_JPEG_QUALITY), 98,
            int(cv2.IMWRITE_JPEG_OPTIMIZE), 1,
            int(cv2.IMWRITE_JPEG_PROGRESSIVE), 1,
        ])
        if not ok:
            raise RuntimeError(f"Could not write {out}")
        print(name, source.shape[1], "x", source.shape[0], "-> 1280 x 720", os.path.getsize(out), "bytes")

    with open(os.path.join(OUT_DIR, ".generated_v0.10.4"), "w", encoding="utf-8") as f:
        f.write("EDSR x4 -> 1280x720, JPEG quality 98, detail restoration\n")


if __name__ == "__main__":
    main()
