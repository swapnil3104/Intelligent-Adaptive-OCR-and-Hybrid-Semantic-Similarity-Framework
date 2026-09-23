import io
import pytest
from PIL import Image
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def create_sample_image(width=200, height=200, format="JPEG", color=(100, 150, 200)):
    """Helper utility to generate a test image in bytes format."""
    file = io.BytesIO()
    image = Image.new("RGB", (width, height), color=color)
    image.save(file, format=format)
    file.seek(0)
    return file.read()


def test_health_check():
    """Verify backend health check endpoint."""
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"


def test_valid_image_upload_jpeg():
    """Test uploading a valid JPEG document image."""
    img_bytes = create_sample_image(300, 400, format="JPEG")
    files = {"file": ("test_document.jpg", img_bytes, "image/jpeg")}
    response = client.post("/api/upload", files=files)
    
    assert response.status_code == 201
    data = response.json()
    assert data["status"] == "success"
    assert data["document"] is not None
    assert data["document"]["original_filename"] == "test_document.jpg"
    assert data["document"]["extension"] == ".jpg"
    assert data["document"]["is_readable"] is True
    assert data["document"]["readability_details"]["width"] == 300
    assert data["document"]["readability_details"]["height"] == 400


def test_valid_image_upload_png():
    """Test uploading a valid PNG document image."""
    img_bytes = create_sample_image(250, 250, format="PNG")
    files = {"file": ("assignment_scan.png", img_bytes, "image/png")}
    response = client.post("/api/upload", files=files)
    
    assert response.status_code == 201
    data = response.json()
    assert data["status"] == "success"
    assert data["document"]["extension"] == ".png"
    assert data["document"]["is_readable"] is True


def test_invalid_file_extension():
    """Test uploading a file with an unsupported file extension."""
    files = {"file": ("malicious_script.sh", b"echo 'hello'", "text/plain")}
    response = client.post("/api/upload", files=files)
    
    assert response.status_code == 422
    data = response.json()
    assert "Unsupported file extension" in data["detail"]


def test_corrupted_image_upload():
    """Test uploading a file with valid extension but corrupted/invalid image binary data."""
    corrupted_bytes = b"NOT_AN_IMAGE_BINARY_DATA_1234567890"
    files = {"file": ("corrupt_photo.jpg", corrupted_bytes, "image/jpeg")}
    response = client.post("/api/upload", files=files)
    
    assert response.status_code == 422
    data = response.json()
    assert "Unreadable or corrupted" in data["detail"] or "too small" in data["detail"]


def test_get_upload_status():
    """Test retrieving upload status and metadata for a previously uploaded document."""
    img_bytes = create_sample_image(150, 150, format="JPEG")
    files = {"file": ("status_test.jpg", img_bytes, "image/jpeg")}
    upload_res = client.post("/api/upload", files=files)
    doc_id = upload_res.json()["document"]["document_id"]

    status_res = client.get(f"/api/upload/{doc_id}")
    assert status_res.status_code == 200
    status_data = status_res.json()
    assert status_data["document"]["document_id"] == doc_id
    assert status_data["document"]["original_filename"] == "status_test.jpg"


def test_preview_document():
    """Test retrieving document preview image."""
    img_bytes = create_sample_image(100, 100, format="JPEG")
    files = {"file": ("preview_test.jpg", img_bytes, "image/jpeg")}
    upload_res = client.post("/api/upload", files=files)
    doc_id = upload_res.json()["document"]["document_id"]

    preview_res = client.get(f"/api/upload/{doc_id}/preview")
    assert preview_res.status_code == 200
    assert len(preview_res.content) > 0
