"""
mini_svg.v2 — Intermedio: añade texto, grupos, polígonos/estrellas y Bézier simple.

Reutiliza TODO lo de v1 (sin duplicar código).
"""

from __future__ import annotations
import math
from typing import List, Optional, Tuple

from .v1 import (  # reexport base
    svg_begin, svg_end, save_svg,
    line, rect, circle,
    _style,
)

__all__ = [
    # v1
    "svg_begin", "svg_end", "save_svg",
    "line", "rect", "circle",
    # v2
    "text", "group",
    "regular_polygon", "star",
    "cubic_bezier",
]


def text(
    x: float, y: float, content: str,
    *, font_size: int = 16, fill: str = "black",
    font_family: str = "sans-serif",
    anchor: str = "start",  # start | middle | end
    opacity: Optional[float] = None
) -> str:
    op = f' opacity="{opacity}"' if opacity is not None else ""
    safe = (
        content.replace("&", "&amp;")
               .replace("<", "&lt;")
               .replace(">", "&gt;")
    )
    return (
        f'<text x="{x}" y="{y}" font-size="{font_size}" fill="{fill}" '
        f'font-family="{font_family}" text-anchor="{anchor}"{op}>{safe}</text>\n'
    )


def group(elements: List[str], *, transform: Optional[str] = None, opacity: Optional[float] = None) -> str:
    t = f' transform="{transform}"' if transform else ""
    op = f' opacity="{opacity}"' if opacity is not None else ""
    return f"<g{t}{op}>\n" + "".join(elements) + "</g>\n"


# --- Coordenadas polares -> cartesianas (para polígonos/estrellas) ---

def _polar_to_xy(cx: float, cy: float, radius: float, angle_deg: float) -> Tuple[float, float]:
    a = math.radians(angle_deg)
    return cx + radius * math.cos(a), cy + radius * math.sin(a)


def regular_polygon(
    n_sides: int,
    bbox: Tuple[float, float, float, float],  # (x,y,w,h)
    rotation_deg: float = 0.0,
    *,
    stroke: str = "black",
    stroke_width: int = 2,
    fill: str = "none",
    opacity: Optional[float] = None
) -> str:
    if n_sides < 3:
        raise ValueError("n_sides debe ser >= 3")

    x, y, w, h = bbox
    cx, cy = x + w / 2, y + h / 2
    radius = min(w, h) / 2

    start = -90.0 + rotation_deg  # “arriba” por defecto
    step = 360.0 / n_sides

    pts = []
    for i in range(n_sides):
        px, py = _polar_to_xy(cx, cy, radius, start + i * step)
        pts.append(f"{px:.2f},{py:.2f}")

    return f'<polygon points="{" ".join(pts)}"{_style(stroke=stroke, stroke_width=stroke_width, fill=fill, opacity=opacity)} />\n'


def star(
    n_points: int,
    bbox: Tuple[float, float, float, float],
    rotation_deg: float = 0.0,
    inner_ratio: float = 0.5,
    *,
    stroke: str = "black",
    stroke_width: int = 2,
    fill: str = "none",
    opacity: Optional[float] = None
) -> str:
    if n_points < 3:
        raise ValueError("n_points debe ser >= 3")
    if not (0.05 <= inner_ratio <= 0.95):
        raise ValueError("inner_ratio debería estar entre 0.05 y 0.95")

    x, y, w, h = bbox
    cx, cy = x + w / 2, y + h / 2
    r_outer = min(w, h) / 2
    r_inner = r_outer * inner_ratio

    start = -90.0 + rotation_deg
    step = 360.0 / (n_points * 2)

    pts = []
    for i in range(n_points * 2):
        r = r_outer if i % 2 == 0 else r_inner
        px, py = _polar_to_xy(cx, cy, r, start + i * step)
        pts.append(f"{px:.2f},{py:.2f}")

    return f'<polygon points="{" ".join(pts)}"{_style(stroke=stroke, stroke_width=stroke_width, fill=fill, opacity=opacity)} />\n'


# --- Bézier simple (1 curva cúbica) ---

def cubic_bezier(
    x0: float, y0: float,
    x1: float, y1: float,
    x2: float, y2: float,
    x3: float, y3: float,
    *,
    stroke: str = "black",
    stroke_width: int = 2,
    fill: str = "none",
    opacity: Optional[float] = None
) -> str:
    d = f"M {x0:.2f},{y0:.2f} C {x1:.2f},{y1:.2f} {x2:.2f},{y2:.2f} {x3:.2f},{y3:.2f}"
    return f'<path d="{d}"{_style(stroke=stroke, stroke_width=stroke_width, fill=fill, opacity=opacity)} />\n'

