# mini-svg

Mini librería educativa para generar gráficos SVG con Python (sin dependencias).
Pensada para practicar bucles, condicionales y funciones creando arte geométrico que luego se abre en Inkscape.

---

## Estructura del repo

```
mini-svg/
  flake.nix
  src/
    mini_svg/
      pyproject.toml
      README.md
      src/
        mini_svg/
          __init__.py
          v1.py
          v2.py
          v3.py
```

---

## Desarrollo con Nix (recomendado)

Desde la raíz del repo:

```
nix develop
```

Prueba rápida:

```
python -c "from mini_svg import v2; print('ok')"
```

(El devShell ya exporta `PYTHONPATH` apuntando a `src/mini_svg/src`.)

---

## Desarrollo con pip / pipenv (sin Nix)

El “root” del proyecto Python está aquí:

```
cd src/mini_svg
```

### pip (editable)

```
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -U pip
pip install -e .
```

### pipenv

```
pipenv --python 3.13
pipenv install --dev
pipenv run python -c "from mini_svg import v2; print('ok')"
```

---

## Versiones / niveles

### v1 — Básico
- svg_begin, svg_end, save_svg
- line, rect, circle

```
from mini_svg import v1
```

### v2 — Intermedio
Añade:
- text, group
- regular_polygon (n lados, bbox, rotación)
- star (n puntas, bbox, rotación)
- cubic_bezier (una curva cúbica)

```
from mini_svg import v2
```

### v3 — Avanzado
Añade:
- bezier_path_cubic (varios segmentos Bézier; introduce listas)

```
from mini_svg import v3
```

---

## Ejemplo mínimo

```
from mini_svg import v1

parts = [v1.svg_begin(400, 200)]
parts.append(v1.circle(200, 100, 40, fill="red"))
parts.append(v1.svg_end())
v1.save_svg("demo.svg", parts)
```

Abre `demo.svg` con Inkscape.

