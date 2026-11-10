import os
import shutil
import subprocess
import hashlib
from manim import SVGMobject

TYPST_BIN = shutil.which("typst") or "typst"
CACHE_DIR = os.path.join(os.path.dirname(__file__), ".typst_cache")

os.makedirs(CACHE_DIR, exist_ok=True)

def tex_to_svg(typst_markup, font_size=28, fill_color="ffffff", max_width=4.5, max_height=0.7):
    key = hashlib.md5(f"{typst_markup}_{font_size}_{fill_color}".encode('utf-8')).hexdigest()
    typ_path = os.path.join(CACHE_DIR, f"{key}.typ")
    svg_path = os.path.join(CACHE_DIR, f"{key}.svg")

    if not os.path.exists(svg_path):
        typ_content = f"#set page(width: auto, height: auto, margin: 6pt, fill: none)\n#set text(fill: rgb(\"{fill_color}\"), size: {font_size}pt)\n\n$ {typst_markup} $\n"
        with open(typ_path, "w", encoding="utf-8") as f:
            f.write(typ_content)

        res = subprocess.run([TYPST_BIN, "compile", typ_path, svg_path], capture_output=True, text=True)
        if res.returncode != 0:
            raise RuntimeError(f"Typst compile failed: {res.stderr}\nCode: {typ_content}")

    svg = SVGMobject(svg_path)
    svg.set_fill(f"#{fill_color}", opacity=1.0)

    if max_height is not None and svg.height > max_height:
        svg.scale_to_fit_height(max_height)
    if max_width is not None and svg.width > max_width:
        svg.scale_to_fit_width(max_width)

    return svg
