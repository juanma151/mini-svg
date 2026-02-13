"""
mini_svg.v1 — Base: SVG como texto, sin dependencias.

Incluye:
  - svg_begin(), svg_end(), save_svg()
  - line(), rect(), circle()
  - estilos básicos (stroke, fill, opacity)
"""

from __future__ import annotations
from typing import List, Optional, Tuple


def svg_begin(width: int, height: int, *, viewbox: Optional[Tuple[int, int, int, int]] = None) -> str:
    if viewbox is None:
        viewbox = (0, 0, width, height)
    x, y, w, h = viewbox
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'width="{width}" height="{height}" '
        f'viewBox="{x} {y} {w} {h}">\n'
    )


def svg_end() -> str:
    return "</svg>\n"


def save_svg(filename: str, parts: List[str]) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        f.write("".join(parts))


def _style(*, stroke: str, stroke_width: int, fill: str, opacity: Optional[float]) -> str:
    op = f' opacity="{opacity}"' if opacity is not None else ""
    return f' stroke="{stroke}" stroke-width="{stroke_width}" fill="{fill}"{op}'


def line(
    x1: float, y1: float, x2: float, y2: float,
    *, stroke: str = "black", stroke_width: int = 2, opacity: Optional[float] = None
) -> str:
    return (
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"'
        f'{_style(stroke=stroke, stroke_width=stroke_width, fill="none", opacity=opacity)} />\n'
    )


def rect(
    x: float, y: float, w: float, h: float,
    *, stroke: str = "black", stroke_width: int = 2, fill: str = "none",
    rx: Optional[float] = None, ry: Optional[float] = None,
    opacity: Optional[float] = None
) -> str:
    r = ""
    if rx is not None:
        r += f' rx="{rx}"'
    if ry is not None:
        r += f' ry="{ry}"'
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}"{r}'
        f'{_style(stroke=stroke, stroke_width=stroke_width, fill=fill, opacity=opacity)} />\n'
    )


def circle(
    cx: float, cy: float, r: float,
    *, stroke: str = "black", stroke_width: int = 2, fill: str = "none",
    opacity: Optional[float] = None
) -> str:
    return (
        f'<circle cx="{cx}" cy="{cy}" r="{r}"'
        f'{_style(stroke=stroke, stroke_width=stroke_width, fill=fill, opacity=opacity)} />\n'
    )

