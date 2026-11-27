from __future__ import annotations
from pathlib import Path

DEFAULT_STARTER_OCR = """// Starter OCR Reference Language file
message = "Hello OCR!"
print(message)
"""
def validate_source_file(source: str | Path) -> Path:
    """Validate that the input file exists, is a file, and uses the .ocr extension."""
    path = Path(source)

    if not path.exists():
        raise FileNotFoundError(f"Source file not found: {path}")
    # Checks that the file exists

    if not path.is_file():
        raise ValueError(f"Source path is not a file: {path}")
    # Checks that the file is a file and not a directory

    if path.suffix != ".ocr":
        raise ValueError(f"Source file must have a .ocr extension: {path}")
    # Checks that the file has a .ocr extension

    return path

def resolve_output_path(source: str | Path, output: str | Path | None) -> Path:
    """Resolve the output path based on the source file and optional output argument."""
    source_path = Path(source)

    if output is not None:
        return Path(output)

    return source_path.with_suffix(".py")

def init_ocr_file(target: str | Path, template: str = DEFAULT_STARTER_OCR) -> Path:
    """Initialize a new OCR file with the given template content."""
    target_path = Path(target)

    if target_path.exists():
        raise FileExistsError(f"Target file already exists: {target_path}")

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(template, encoding="utf-8")
    return target_path

def read_source_file(source: str | Path) -> str:
    """Read the contents of the source OCR file"""
    source_path = validate_source_file(source)
    return source_path.read_text(encoding="utf-8")

def write_output_file(output: str | Path, content: str) -> Path:
    """Write the generated Python code to the output file"""
    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")
    return output_path

    