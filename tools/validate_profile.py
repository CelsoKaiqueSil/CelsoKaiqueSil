"""Validate the profile's local references and PNG without dependencies."""

from pathlib import Path
import re
import struct
import zlib

ROOT = Path(__file__).resolve().parents[1]


def validate():
    assets = [ROOT / "assets/header.png", *sorted((ROOT / "assets/projects").glob("*.png"))]
    assert len(assets) == 5, "Expected a header and four project covers"
    for path in assets:
        validate_png(path)
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for ref in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", readme):
        assert not ref.startswith("http"), "Use local profile imagery"
        assert (ROOT / ref).is_file(), ref
    assert len(readme.splitlines()) <= 80, "Keep the profile concise"
    assert readme.count("### [") == 4
    assert "shields.io" not in readme
    assert "homologa\u00e7\u00e3o no Desktop" in readme
    print("Profile validated: five PNG assets and four projects.")


def validate_png(path):
    data = path.read_bytes()
    assert data[:8] == b"\x89PNG\r\n\x1a\n", "Invalid PNG signature"
    assert len(data) < 4_000_000, "Keep the header lightweight"
    offset, ended = 8, False
    while offset < len(data):
        length = struct.unpack(">I", data[offset:offset+4])[0]
        kind = data[offset+4:offset+8]
        payload = data[offset+8:offset+8+length]
        checksum = struct.unpack(">I", data[offset+8+length:offset+12+length])[0]
        assert zlib.crc32(kind+payload) == checksum, "Damaged PNG chunk"
        offset += length + 12
        if kind == b"IEND":
            ended = True
            break
    assert ended and offset == len(data), "Truncated PNG or trailing bytes"
    width, height = struct.unpack(">II", data[16:24])
    assert width >= 1200 and 2.8 <= width/height <= 3.2
    print(f"PNG validated: {path.name}, {width}x{height}, {len(data):,} bytes.")


if __name__ == "__main__":
    validate()
