# mini-svg

Mini librería educativa para generar gráficos SVG con Python.  
Pensada para trabajar programación estructurada (bucles, condicionales, funciones) creando arte geométrico exportable a Inkscape.

---

## 📦 Instalación (modo desarrollo)

### Opción A — Nix + direnv (recomendado si usas Nix)

```
direnv allow
```

Comprobar que funciona:

```
python -c "from mini_svg import v2; print('ok')"
```

Ejecutar un ejemplo:

```
python examples/01_basico_patron.py
```

En este modo, el `PYTHONPATH` se configura automáticamente para usar `src/`.

---

### Opción B — Pipenv

Crear entorno:

```
pipenv --python 3.13
pipenv install --dev
```

Entrar en el entorno:

```
pipenv shell
```

Comprobar import:

```
python -c "from mini_svg import v2; print('ok')"
```

Ejecutar ejemplo:

```
python examples/01_basico_patron.py
```

---

## 🐍 Instalación clásica con pip

```
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -U pip
pip install -e .
```

---

## 📁 Estructura del proyecto

```
mini-svg/
  flake.nix
  pyproject.toml
  README.md
  src/
    mini_svg/
      __init__.py
      v1.py
      v2.py
      v3.py
  examples/
```

---

## 🧩 Versiones de la librería

### v1 — Básico
Incluye:
- svg_begin
- svg_end
- save_svg
- line
- rect
- circle

Uso:

```
from mini_svg import v1
```

---

### v2 — Intermedio
Añade:
- text
- group
- regular_polygon
- star
- cubic_bezier

Uso:

```
from mini_svg import v2
```

---

### v3 — Avanzado
Añade:
- bezier_path_cubic (curvas múltiples con listas)

Uso:

```
from mini_svg import v3
```

---

## 🧠 Filosofía del diseño

- v2 importa todo lo de v1.
- v3 importa todo lo de v2.
- No hay duplicación de código.
- mini_svg (monolítico) exporta todo lo de v3.

---

## 🎨 Ejemplo mínimo

```
from mini_svg import v1

parts = [v1.svg_begin(400, 200)]
parts.append(v1.circle(200, 100, 40, fill="red"))
parts.append(v1.svg_end())

v1.save_svg("demo.svg", parts)
```

Abre `demo.svg` con Inkscape.

