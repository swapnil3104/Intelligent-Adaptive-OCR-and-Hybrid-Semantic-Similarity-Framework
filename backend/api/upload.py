import os
from fastapi import APIRouter, File, UploadFile, HTTPException, status
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
from typing import Dict, Any, Optional

from backend.services.upload_service import (
    process_and_store_upload,
    get_document_by_id,
    DocumentMetadata,
)

router = APIRouter(prefix="/upload", tags=["Document Upload"])


class UploadResponse(BaseModel):
    status: str
    message: str
    document: Optional[DocumentMetadata] = None


@router.post("", response_model=UploadResponse, status_code=status.HTTP_201_CREATED)
async def upload_document(file: UploadFile = File(...)):
    """
    Module 1: Document Upload Endpoint
    Validates document image format, readability, saves safely to temporary storage,
    and returns upload status + metadata.
    """
    if not file or not file.filename:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No file provided in request.",
        )

    try:
        contents = await file.read()
        result = process_and_store_upload(contents, file.filename)

        if not result["success"]:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=result["error"],
            )

        return UploadResponse(
            status="success",
            message="Document uploaded and validated successfully.",
            document=result["document"],
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred during document upload: {str(e)}",
        )


@router.get("/{document_id}", response_model=UploadResponse)
async def get_upload_status(document_id: str):
    """
    Retrieve document upload metadata and readability status by document ID.
    """
    doc = get_document_by_id(document_id)
    if not doc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Document with ID '{document_id}' not found.",
        )

    return UploadResponse(
        status="success",
        message="Document details retrieved successfully.",
        document=doc,
    )


@router.get("/{document_id}/preview")
async def preview_document(document_id: str):
    """
    Stream/serve raw uploaded document image for preview.
    """
    doc = get_document_by_id(document_id)
    if not doc or not os.path.exists(doc.file_path):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Document preview not available for ID '{document_id}'.",
        )

    return FileResponse(doc.file_path, filename=doc.original_filename)
