import uuid
import hashlib
import time
from pathlib import Path
from typing import Dict, Any, Optional
from pydantic import BaseModel, Field

from backend.config.settings import UPLOAD_DIR
from backend.utils.validation import (
    validate_file_extension,
    validate_file_size,
    validate_image_readability,
)


class DocumentMetadata(BaseModel):
    document_id: str
    original_filename: str
    stored_filename: str
    file_path: str
    file_size_bytes: int
    extension: str
    sha256_checksum: str
    upload_timestamp: float
    is_readable: bool
    readability_details: Dict[str, Any]


# In-memory database repository for document uploads
UPLOADED_DOCUMENTS_DB: Dict[str, DocumentMetadata] = {}


def process_and_store_upload(
    file_bytes: bytes, filename: str
) -> Dict[str, Any]:
    """
    Validates file extension, size, image readability, saves file to storage,
    and returns a structured metadata dictionary.
    """
    # 1. Extension Validation
    if not validate_file_extension(filename):
        ext = Path(filename).suffix
        return {
            "success": False,
            "error": f"Unsupported file extension '{ext}'. Allowed extensions are: JPG, PNG, BMP, TIFF, WEBP, PDF.",
            "document": None,
        }

    # 2. File Size Validation
    file_size = len(file_bytes)
    is_size_valid, size_error = validate_file_size(file_size)
    if not is_size_valid:
        return {
            "success": False,
            "error": size_error,
            "document": None,
        }

    # 3. Compute Checksum
    sha256_checksum = hashlib.sha256(file_bytes).hexdigest()

    # 4. Image Readability Validation
    readability_result = validate_image_readability(file_bytes)
    if not readability_result["is_readable"]:
        return {
            "success": False,
            "error": readability_result["error"],
            "document": None,
        }

    # 5. Generate Unique Storage Path
    document_id = f"doc_{uuid.uuid4().hex[:12]}"
    ext = Path(filename).suffix.lower()
    stored_filename = f"{document_id}{ext}"
    file_path = UPLOAD_DIR / stored_filename

    # Save to disk
    with open(file_path, "wb") as f:
        f.write(file_bytes)

    # 6. Construct Document Metadata
    metadata = DocumentMetadata(
        document_id=document_id,
        original_filename=filename,
        stored_filename=stored_filename,
        file_path=str(file_path),
        file_size_bytes=file_size,
        extension=ext,
        sha256_checksum=sha256_checksum,
        upload_timestamp=time.time(),
        is_readable=readability_result["is_readable"],
        readability_details=readability_result,
    )

    # Store in memory repository
    UPLOADED_DOCUMENTS_DB[document_id] = metadata

    return {
        "success": True,
        "error": None,
        "document": metadata,
    }


def get_document_by_id(document_id: str) -> Optional[DocumentMetadata]:
    """Retrieve document metadata by document ID."""
    return UPLOADED_DOCUMENTS_DB.get(document_id)
