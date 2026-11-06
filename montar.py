"""Gera index.html com as imagens embutidas, para funcionar em um arquivo só."""
import base64
import pathlib
import re

base = pathlib.Path(__file__).parent
html = (base / "fonte.html").read_text(encoding="utf-8")


def embed(match):
    data = (base / "img" / f"{match.group(1)}.jpg").read_bytes()
    return "data:image/jpeg;base64," + base64.b64encode(data).decode()


out = re.sub(r"\{\{img:([\w-]+)\}\}", embed, html)
(base / "index.html").write_text(out, encoding="utf-8")
print(f"index.html: {len(out) / 1024 / 1024:.2f} MiB")
