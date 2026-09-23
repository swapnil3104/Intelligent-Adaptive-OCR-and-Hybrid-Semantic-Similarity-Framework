# Intelligent Adaptive OCR and Hybrid Semantic Similarity Framework

> **Project Type:** Final Year B.Tech CSE Mega Project (Academic Year 2025–26)  
> **Institution:** Annasaheb Dange College of Engineering and Technology, Ashta  
> **Department:** Computer Science & Engineering  

---

## 📌 Executive Summary

The **Intelligent Adaptive OCR and Hybrid Semantic Similarity Framework** is an end-to-end AI-powered plagiarism detection system engineered specifically for **handwritten, scanned, and printed documents**.

Traditional plagiarism detectors excel with digital text but struggle when faced with handwritten submissions, low-resolution scans, noisy images, or paraphrased content. This framework addresses these challenges by integrating **image preprocessing, adaptive OCR engine selection, vector-based semantic retrieval, lexical matching, semantic embedding similarity, and contextual cross-encoder reranking** into a unified, high-accuracy pipeline.

---

## 🎯 Key Features

1. **Adaptive Image Preprocessing & Restoration**
   - Quality assessment (Laplacian blur variance, contrast evaluation, noise estimation).
   - Dynamic preprocessing pipeline (Adaptive thresholding, Bilateral filtering, Deskewing, Contrast Adjustment).

2. **Multi-Engine Adaptive OCR Selection**
   - Automated routing between OCR engines (**Tesseract**, **PaddleOCR**, **TrOCR**, **EasyOCR**) based on document type (handwritten vs. printed) and quality score.
   - Text extraction paired with segment-level OCR confidence scoring.

3. **Two-Stage Candidate Retrieval**
   - High-speed vector retrieval using **Sentence-BERT (SBERT)** embeddings and vector stores (**FAISS / ChromaDB**).
   - Efficient filtering of reference database documents prior to deep similarity computation.

4. **Multi-Layer Hybrid Similarity Engine**
   - **Lexical Similarity:** TF-IDF vectorization and Cosine Similarity for exact phrase and keyword matching.
   - **Semantic Similarity:** Dense vector representation using SBERT embeddings for structural similarity.
   - **Contextual Reranking:** Fine-grained sentence/paragraph analysis using Transformer **Cross-Encoders**.

5. **OCR-Aware Plagiarism Scoring**
   - Adaptive weighting mechanism that adjusts plagiarism confidence based on OCR accuracy scores.

6. **Interactive Dashboard & Comprehensive Reporting**
   - Detailed visual breakdown highlighting exact lexical matches, paraphrased sections, and overall similarity scores.

---

## 🏗️ Pipeline Architecture

```text
Document Image Input (Handwritten / Scanned / Printed)
   │
   ▼
[ 1. Image Preprocessing & Quality Assessment ]
   │
   ▼
[ 2. Adaptive OCR Engine Selection (Tesseract / PaddleOCR / TrOCR) ]
   │
   ▼
[ 3. Extracted Text + Segment Confidence Scores ]
   │
   ▼
[ 4. Text Cleaning & Preprocessing ]
   │
   ▼
[ 5. Vector Store Candidate Retrieval (SBERT + FAISS/ChromaDB) ]
   │
   ▼
[ 6. Hybrid Similarity Engine ]
   ├── Lexical Analysis (TF-IDF & Cosine Similarity)
   ├── Semantic Analysis (SBERT Embeddings)
   └── Contextual Analysis (Cross-Encoder Reranking)
   │
   ▼
[ 7. Weighted Plagiarism & Confidence Scoring ]
   │
   ▼
[ 8. Interactive Report & Highlight Visualizer ]
```

---

## 📚 Project Documentation

The repository includes comprehensive architectural, requirement, and design specifications:

- 📄 **[Product Requirements Document (PRD)](PRD_Intelligent_Adaptive_OCR_Hybrid_Semantic_Similarity.md)** – Detailed product goals, functional/non-functional requirements, user stories, and acceptance criteria.
- 📐 **[Architecture Specification](architecture.md)** – System components, pipeline flow, error handling strategy, and deployment topology.
- 🎨 **[System Design Specification](DESIGN.md)** – Detailed module designs, database schemas, algorithm choices, and API specifications.
- 📜 **[Development Rules](DEVELOPMENT_RULES.md)** – Coding standards, git conventions, safety guidelines, and testing requirements.
- 📋 **[Tasks & Roadmap](TASKS.md)** – Complete breakdown of implementation phases, task statuses, and milestones.

---

## 🛠️ Technology Stack

| Layer | Technologies & Frameworks |
| :--- | :--- |
| **Language & Core** | Python 3.10+, PyTorch, NumPy, Pandas |
| **Computer Vision / OCR** | OpenCV, PIL, Tesseract, PaddleOCR, Hugging Face TrOCR, EasyOCR |
| **NLP & Semantics** | Hugging Face Transformers, Sentence-Transformers (SBERT), Scikit-Learn |
| **Vector DB & Retrieval** | FAISS / ChromaDB |
| **Backend & API** | FastAPI / Flask |
| **Frontend & UI** | React / Modern Dashboard |

---

## 📁 Repository Structure

```text
├── .gitignore                                           # Git ignore configuration
├── README.md                                            # Project overview & quickstart guide
├── PRD_Intelligent_Adaptive_OCR_Hybrid_Semantic_Similarity.md # Product Requirements Document
├── architecture.md                                      # System Architecture Specification
├── DESIGN.md                                            # Detailed System Design & Module Docs
├── DEVELOPMENT_RULES.md                                 # Development rules & coding guidelines
└── TASKS.md                                             # Implementation roadmap & task tracking
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher
- Git
- Tesseract OCR engine (installed on system PATH)

### Installation (Draft Setup)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/swapnil3104/Intelligent-Adaptive-OCR-and-Hybrid-Semantic-Similarity-Framework.git
   cd Intelligent-Adaptive-OCR-and-Hybrid-Semantic-Similarity-Framework
   ```

2. **Set up virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On Linux/macOS:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install --upgrade pip
   # Requirements file will be updated during implementation phase
   ```

---

## 🤝 Contributing & Guidelines

Please read **[DEVELOPMENT_RULES.md](DEVELOPMENT_RULES.md)** prior to submitting pull requests or making modifications to code logic.

---

## 📄 License

Academic / Institutional Research Project — Annasaheb Dange College of Engineering and Technology (2025–26).
