{
  description = "mini-svg — devshell reproducible (nixos-unstable + python313)";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs }:
  let
    systems = [ "x86_64-linux" "aarch64-linux" "x86_64-darwin" "aarch64-darwin" ];
    forAllSystems = f: nixpkgs.lib.genAttrs systems (system: f system);
  in
  {
    devShells = forAllSystems (system:
      let
        pkgs = import nixpkgs { inherit system; };

        # Si tu snapshot no tiene python313, cambia a python312.
        python = pkgs.python313;
      in
      {
        default = pkgs.mkShell {
          name = "mini-svg";

          packages = [
            python
            python.pkgs.pip
            python.pkgs.setuptools
            python.pkgs.wheel
            python.pkgs.pytest
            python.pkgs.ruff
            python.pkgs.black
            python.pkgs.mypy
            python.pkgs.build
            python.pkgs.twine
            pkgs.pipenv
            pkgs.git
          ];

          shellHook = ''
            # Subproyecto Python (con guion) vive aquí:
            export MINI_SVG_PROJECT_ROOT="$PWD/src/mini-svg"

            # El paquete importable "mini_svg" está dentro de:
            #   $MINI_SVG_PROJECT_ROOT/src/mini_svg
            # Por tanto, PYTHONPATH debe incluir:
            #   $MINI_SVG_PROJECT_ROOT/src
            export PYTHONPATH="$MINI_SVG_PROJECT_ROOT/src''${PYTHONPATH:+:}$PYTHONPATH"

            echo "✅ mini-svg devShell listo"
            echo "   Project root: $MINI_SVG_PROJECT_ROOT"
            echo "   PYTHONPATH:   $PYTHONPATH"
            python -c "from mini_svg import v2; print('mini_svg import OK')"
          '';
        };
      }
    );
  };
}

