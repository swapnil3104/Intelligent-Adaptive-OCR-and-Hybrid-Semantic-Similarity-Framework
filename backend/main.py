import os
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from backend.api.upload import router as upload_router

app = FastAPI(
    title="Intelligent Adaptive OCR and Hybrid Semantic Similarity Framework",
    description="AI-driven plagiarism detection pipeline for handwritten, scanned, and printed documents.",
    version="1.0.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API Routers
app.include_router(upload_router, prefix="/api")


@app.get("/api/health")
async def health_check():
    """Health check endpoint to verify backend operational status."""
    return {
        "status": "healthy",
        "framework": "Intelligent Adaptive OCR & Hybrid Semantic Similarity",
        "version": "1.0.0",
    }


# Serve frontend directory if present
FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"
if (FRONTEND_DIR / "index.html").exists():
    app.mount("/", StaticFiles(directory=str(FRONTEND_DIR), html=True), name="frontend")



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)
