"""
mini_svg.v3 — Avanzado: añade rutas Bézier múltiples (listas de segmentos).

Reutiliza TODO lo de v2 (y por extensión v1).
"""

from __future__ import annotations
from typing import List, Optional, Tuple

from .v2 import *  # reexporta todo lo de v2 (incluye v1)
from .v2 import _style  # para construir el <path> con estilo

__all__ = list(globals().get("__all__", [])) + ["bezier_path_cubic"]


def bezier_path_cubic(
    start: Tuple[float, float],
    segments: List[Tuple[float, float, float, float, float, float]],
    *,
    closed: bool = False,
    stroke: str = "black",
    stroke_width: int = 2,
    fill: str = "none",
    opacity: Optional[float] = None
) -> str:
    """
    start = (x0,y0)
    segments = [(cx1,cy1,cx2,cy2,x,y), ...]  # cada tupla añade un 'C'
    """
    x0, y0 = start
    d_parts = [f"M {x0:.2f},{y0:.2f}"]
    for (cx1, cy1, cx2, cy2, x, y) in segments:
        d_parts.append(f"C {cx1:.2f},{cy1:.2f} {cx2:.2f},{cy2:.2f} {x:.2f},{y:.2f}")
    if closed:
        d_parts.append("Z")

    d = " ".join(d_parts)
    return f'<path d="{d}"{_style(stroke=stroke, stroke_width=stroke_width, fill=fill, opacity=opacity)} />\n'

