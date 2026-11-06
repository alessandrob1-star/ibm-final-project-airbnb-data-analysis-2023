"""Validate the saved notebook and assets without executing dataset analysis."""

from __future__ import annotations

import ast
import base64
import hashlib
import io
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

import matplotlib
import nbformat
import notebook
import numpy
import pandas
import seaborn
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    # Import the actual analysis dependencies and check the option used by the notebook.
    pandas.set_option("future.no_silent_downcasting", True)
    print("Dependency imports: OK")
    for module in (pandas, numpy, matplotlib, seaborn, notebook, nbformat):
        print(f"  {module.__name__}: {module.__version__}")

    notebooks = sorted(ROOT.glob("*.ipynb"))
    if not notebooks:
        raise ValueError("No notebook found in the repository root")
    saved_images: set[str] = set()
    code_cells = 0
    for path in notebooks:
        document = nbformat.read(path, as_version=4)
        nbformat.validate(document)
        for index, cell in enumerate(document.cells):
            if cell.cell_type != "code":
                continue
            ast.parse(cell.source, filename=f"{path.name}:cell-{index}")
            code_cells += 1
            for output in cell.get("outputs", []):
                encoded = output.get("data", {}).get("image/png")
                if encoded is None:
                    continue
                if isinstance(encoded, list):
                    encoded = "".join(encoded)
                data = base64.b64decode("".join(encoded.split()), validate=True)
                with Image.open(io.BytesIO(data)) as image:
                    image.verify()
                saved_images.add(hashlib.sha256(data).hexdigest())
        print(f"Notebook structure and code syntax: {path.name}: OK")
    if code_cells == 0:
        raise ValueError("The notebook has no code cells")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    references: set[Path] = set()
    # Check local Markdown links and images; external URLs are deliberately not fetched.
    for target in re.findall(r"\]\(([^)]+)\)", readme):
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        path = (ROOT / unquote(parsed.path)).resolve()
        if not path.is_relative_to(ROOT):
            raise ValueError(f"README target escapes the repository: {target}")
        if not path.exists():
            raise ValueError(f"Missing README target: {target}")
        references.add(path)
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif"}:
            with Image.open(path) as image:
                image.verify()

    figures = sorted((ROOT / "docs" / "figures").glob("*.png"))
    for path in figures:
        if path.resolve() not in references:
            raise ValueError(f"Exported figure is not linked in README: {path.name}")
        if hashlib.sha256(path.read_bytes()).hexdigest() not in saved_images:
            raise ValueError(f"Figure does not match any saved notebook output: {path.name}")
    print(f"Local README links and images: {len(references)} valid targets")
    print(f"Published figures matching saved outputs: {len(figures)}")
    print("No notebook cells were executed; the external dataset and analytical conclusions were not validated.")


if __name__ == "__main__":
    main()
