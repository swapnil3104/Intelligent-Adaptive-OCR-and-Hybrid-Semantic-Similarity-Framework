import os
import io
from pathlib import Path
from typing import Tuple, Dict, Any, Optional
from PIL import Image, ImageOps
from backend.config.settings import (
    ALLOWED_EXTENSIONS,
    ALLOWED_MIME_TYPES,
    MAX_FILE_SIZE_BYTES,
    MIN_IMAGE_WIDTH,
    MIN_IMAGE_HEIGHT,
)


def validate_file_extension(filename: str) -> bool:
    """Check if the file extension is in the list of allowed extensions."""
    ext = Path(filename).suffix.lower()
    return ext in ALLOWED_EXTENSIONS


def validate_file_size(file_size: int) -> Tuple[bool, Optional[str]]:
    """Validate that file size does not exceed the allowed maximum."""
    if file_size <= 0:
        return False, "File is empty (0 bytes)."
    if file_size > MAX_FILE_SIZE_BYTES:
        max_mb = MAX_FILE_SIZE_BYTES / (1024 * 1024)
        return False, f"File size exceeds maximum allowed limit of {max_mb:.1f} MB."
    return True, None


def validate_image_readability(file_source: Any) -> Dict[str, Any]:
    """
    Validate that the uploaded file can be opened and read as an image.
    Extracts key metadata such as dimensions, format, mode, and readability status.
    
    Accepts a file path (str/Path) or file-like bytes object.
    """
    try:
        if isinstance(file_source, (str, Path)):
            image = Image.open(file_source)
        elif isinstance(file_source, bytes):
            image = Image.open(io.BytesIO(file_source))
        else:
            image = Image.open(file_source)

        # Verify image integrity
        image.verify()

        # Re-open after verify() as PIL requires
        if isinstance(file_source, (str, Path)):
            image = Image.open(file_source)
        elif isinstance(file_source, bytes):
            image = Image.open(io.BytesIO(file_source))
        else:
            file_source.seek(0)
            image = Image.open(file_source)

        width, height = image.size
        img_format = image.format or "UNKNOWN"
        img_mode = image.mode

        if width < MIN_IMAGE_WIDTH or height < MIN_IMAGE_HEIGHT:
            return {
                "is_readable": False,
                "error": f"Image resolution ({width}x{height}) is too small for OCR processing (min {MIN_IMAGE_WIDTH}x{MIN_IMAGE_HEIGHT}).",
                "width": width,
                "height": height,
                "format": img_format,
                "mode": img_mode,
            }

        return {
            "is_readable": True,
            "error": None,
            "width": width,
            "height": height,
            "format": img_format,
            "mode": img_mode,
            "channels": len(image.getbands()),
        }
    except Exception as e:
        return {
            "is_readable": False,
            "error": f"Unreadable or corrupted image file: {str(e)}",
            "width": 0,
            "height": 0,
            "format": None,
            "mode": None,
            "channels": 0,
        }
