# Product Requirements Document (PRD)

# Intelligent Adaptive OCR and Hybrid Semantic Similarity Framework

> **Project Type:** Final Year B.Tech CSE Mega Project\
> **Document Type:** Project-Level PRD\
> **Status:** Draft\
> **Version:** 1.0\
> **Academic Year:** 2025--26\
> **Institution:** Annasaheb Dange College of Engineering and
> Technology, Ashta\
> **Department:** Computer Science & Engineering

------------------------------------------------------------------------

## 1. Executive Summary

### 1.1 Project Overview

The **Intelligent Adaptive OCR and Hybrid Semantic Similarity
Framework** is an AI-based plagiarism detection system designed to
analyze **handwritten, scanned, and printed documents**.

Traditional plagiarism detection systems generally perform well on
digitally typed text but face difficulties when the input is
handwritten, scanned, noisy, or paraphrased. This project addresses
these limitations by combining **image preprocessing, adaptive Optical
Character Recognition (OCR), semantic retrieval, lexical similarity,
semantic similarity, and contextual similarity** into a single
framework.

The proposed system first improves the quality of an input document
image, selects a suitable OCR engine, extracts text with an OCR
confidence score, retrieves potentially similar documents using
Sentence-BERT (SBERT), and then performs hybrid plagiarism analysis
using **TF-IDF, cosine similarity, SBERT, and a Cross-Encoder**.

The final system produces a **plagiarism score** based on the
combination of OCR confidence and multiple similarity measures.

------------------------------------------------------------------------

## 2. Problem Statement

Existing plagiarism detection systems have several limitations:

-   Limited support for handwritten documents.
-   Reduced OCR accuracy on poor-quality images and complex handwriting.
-   Difficulty detecting paraphrased or semantically similar content.
-   Heavy dependence on exact word matching.
-   Separate handling of OCR and plagiarism detection.
-   Limited ability to compare handwritten, scanned, and typed documents
    in one framework.
-   Increased processing time for large document collections.
-   Reduced performance on documents containing complex layouts,
    diagrams, tables, or low-resolution images.

### Problem Definition

Develop an intelligent framework that can extract text from handwritten
and scanned documents using adaptive OCR and detect both **direct and
paraphrased plagiarism** using a hybrid lexical, semantic, and
contextual similarity approach.

------------------------------------------------------------------------

## 3. Product Vision

Build a unified document analysis framework that can:

1.  Accept handwritten, scanned, or printed documents.
2.  Improve document quality before OCR.
3.  Automatically select an appropriate OCR engine.
4.  Extract text and OCR confidence.
5.  Retrieve semantically similar documents.
6.  Detect direct and paraphrased plagiarism.
7.  Generate an interpretable final plagiarism score.
8.  Provide evaluation metrics for measuring system performance.

------------------------------------------------------------------------

## 4. Target Users

### 4.1 Students

Students can use the system to check whether assignments, notes,
reports, or handwritten submissions contain content similar to existing
documents.

### 4.2 Faculty Members

Faculty can analyze handwritten or scanned assignments and identify
potentially copied content.

### 4.3 Academic Institutions

Universities and colleges can use the framework as a foundation for
academic-integrity and document-analysis systems.

### 4.4 Researchers

Researchers can use the framework to experiment with OCR, semantic
retrieval, and plagiarism detection techniques.

------------------------------------------------------------------------

## 5. Goals and Objectives

### 5.1 Primary Goal

Develop an intelligent plagiarism detection framework capable of
handling handwritten, scanned, and printed documents while detecting
both exact and paraphrased plagiarism.

### 5.2 Objectives

-   Improve handwritten text extraction using image preprocessing and
    adaptive OCR.
-   Implement adaptive OCR using Tesseract, EasyOCR, and TrOCR.
-   Record OCR confidence for extracted text.
-   Generate semantic embeddings using Sentence-BERT.
-   Retrieve the top-k most similar documents.
-   Implement lexical similarity using TF-IDF and cosine similarity.
-   Implement semantic similarity using SBERT.
-   Implement contextual similarity using a Cross-Encoder.
-   Combine multiple similarity signals into a hybrid plagiarism score.
-   Integrate OCR confidence with similarity scores.
-   Evaluate the system using OCR accuracy, Precision, Recall, F1-score,
    Accuracy, cosine similarity, processing time, and final plagiarism
    score.

------------------------------------------------------------------------

# 6. Scope

## 6.1 In Scope

### Document Input

-   Handwritten images.
-   Scanned documents.
-   Printed documents.
-   Image-based academic documents.

### Image Processing

-   Grayscale conversion.
-   Noise removal.
-   Binarization.
-   Skew correction.
-   Contrast enhancement.

### OCR

-   Tesseract OCR.
-   EasyOCR.
-   TrOCR.
-   Adaptive OCR selection.
-   OCR confidence extraction.

### NLP

-   Text normalization.
-   Lowercasing.
-   Punctuation removal.
-   Tokenization.
-   Stop-word removal.
-   Lemmatization.

### Semantic Retrieval

-   Sentence-BERT embeddings.
-   Cosine similarity.
-   Top-k similar document retrieval.

### Plagiarism Detection

-   TF-IDF.
-   Lexical cosine similarity.
-   SBERT semantic similarity.
-   Cross-Encoder contextual similarity.
-   Hybrid similarity calculation.
-   Final plagiarism scoring.

### Evaluation

-   OCR Accuracy.
-   Precision.
-   Recall.
-   F1-score.
-   Accuracy.
-   Cosine Similarity.
-   Processing Time.
-   Final Plagiarism Score.

------------------------------------------------------------------------

## 6.2 Future Scope

The framework may later be extended to:

-   Multilingual document processing.
-   Larger document repositories.
-   Cloud-based plagiarism detection.
-   More OCR engines.
-   More advanced handwriting recognition.
-   Advanced vector databases.
-   Institution-wide document repositories.
-   Additional document formats.
-   Improved explainability and plagiarism highlighting.

------------------------------------------------------------------------

# 7. Product Workflow

``` text
                  ┌──────────────────────┐
                  │   Upload Document    │
                  └──────────┬───────────┘
                             ↓
                  ┌──────────────────────┐
                  │ Image Preprocessing  │
                  │ Gray / Denoise /     │
                  │ Threshold / Deskew   │
                  └──────────┬───────────┘
                             ↓
                  ┌──────────────────────┐
                  │    Adaptive OCR      │
                  │ Tesseract / EasyOCR  │
                  │      / TrOCR         │
                  └──────────┬───────────┘
                             ↓
                  ┌──────────────────────┐
                  │ Extracted Text +     │
                  │ OCR Confidence       │
                  └──────────┬───────────┘
                             ↓
                  ┌──────────────────────┐
                  │ Text Preprocessing   │
                  └──────────┬───────────┘
                             ↓
                  ┌──────────────────────┐
                  │      SBERT           │
                  │ Semantic Embeddings  │
                  └──────────┬───────────┘
                             ↓
                  ┌──────────────────────┐
                  │ Top-K Similar Docs   │
                  └──────────┬───────────┘
                             ↓
             ┌───────────────┼────────────────┐
             ↓               ↓                ↓
       ┌───────────┐   ┌───────────┐   ┌─────────────┐
       │ TF-IDF +  │   │   SBERT   │   │Cross-Encoder│
       │ Cosine    │   │Similarity │   │ Similarity  │
       └─────┬─────┘   └─────┬─────┘   └──────┬──────┘
             └───────────────┼────────────────┘
                             ↓
                  ┌──────────────────────┐
                  │ Hybrid Scoring       │
                  │ + OCR Confidence     │
                  └──────────┬───────────┘
                             ↓
                  ┌──────────────────────┐
                  │ Final Plagiarism     │
                  │       Score          │
                  └──────────────────────┘
```

------------------------------------------------------------------------

# 8. System Modules

## Module 1 --- Document Upload

### Purpose

Accept document images as input.

### Requirements

-   Accept image-based documents.
-   Validate file type.
-   Validate image readability.
-   Store the input temporarily for processing.
-   Display upload status.

### Output

A valid document image ready for preprocessing.

------------------------------------------------------------------------

## Module 2 --- Image Preprocessing

### Purpose

Improve document quality before OCR.

### Processing Pipeline

``` text
Input Image
    ↓
Grayscale
    ↓
Noise Removal
    ↓
Binarization
    ↓
Skew Correction
    ↓
Contrast Enhancement
    ↓
Processed Image
```

### Acceptance Criteria

-   The system should successfully preprocess supported document images.
-   Each preprocessing operation should be independently testable.
-   The processed image should be available for OCR.

------------------------------------------------------------------------

## Module 3 --- Adaptive OCR

### Purpose

Extract text from documents while selecting an appropriate OCR engine.

### OCR Engines

  OCR Engine   Intended Use
  ------------ --------------------------
  Tesseract    Printed text
  EasyOCR      Complex image-based text
  TrOCR        Handwritten text

### Output

``` json
{
  "extracted_text": "...",
  "ocr_engine": "TrOCR",
  "ocr_confidence": 0.00
}
```

The actual confidence format and scale should be finalized during
implementation based on the selected OCR engine.

------------------------------------------------------------------------

## Module 4 --- Text Preprocessing

### Operations

-   Lowercasing.
-   Punctuation removal.
-   Tokenization.
-   Stop-word removal.
-   Lemmatization.

### Output

Clean normalized text suitable for similarity analysis.

------------------------------------------------------------------------

## Module 5 --- Semantic Retrieval

### Purpose

Efficiently identify potentially similar documents from the document
repository.

### Process

``` text
Clean Text
    ↓
SBERT
    ↓
Sentence Embedding
    ↓
Cosine Similarity
    ↓
Top-K Similar Documents
```

### Requirements

-   Generate an embedding for the uploaded document.
-   Compare the embedding against repository documents.
-   Rank candidate documents by similarity.
-   Return top-k candidates.

------------------------------------------------------------------------

# 9. Hybrid Plagiarism Detection

## 9.1 Lexical Similarity

Use **TF-IDF** and **cosine similarity** to measure lexical overlap.

This component is useful for detecting content that shares similar words
or phrases.

------------------------------------------------------------------------

## 9.2 Semantic Similarity

Use **Sentence-BERT** to compare the semantic meaning of document
content.

This component helps identify content that may express similar ideas
using different wording.

------------------------------------------------------------------------

## 9.3 Contextual Similarity

Use a **Cross-Encoder** based on MiniLM/BERT or an equivalent selected
model to perform contextual pairwise comparison.

------------------------------------------------------------------------

## 9.4 Hybrid Similarity

The final plagiarism analysis should combine:

``` text
Lexical Similarity
        +
Semantic Similarity
        +
Contextual Similarity
        ↓
Hybrid Similarity
```

The exact weights must be determined experimentally during evaluation.

------------------------------------------------------------------------

# 10. Final Plagiarism Score

The system will combine OCR confidence and multiple similarity signals
using a weighted scoring mechanism.

Conceptually:

``` text
OCR Confidence
      +
Lexical Similarity
      +
Semantic Similarity
      +
Cross-Encoder Similarity
      ↓
Weighted Scoring Mechanism
      ↓
Final Plagiarism Score
```

### Important Requirement

The weighting strategy should be configurable during experimentation and
should be validated against the prepared evaluation dataset.

The PRD does not prescribe fixed weights because the project synopsis
does not specify validated numerical weights.

------------------------------------------------------------------------

# 11. User Stories

## US-01 --- Upload Document

**As a** student or faculty member,\
**I want** to upload a handwritten, scanned, or printed document,\
**so that** the system can analyze it for plagiarism.

### Acceptance Criteria

-   [ ] User can select a supported document image.
-   [ ] Invalid files are rejected.
-   [ ] Uploaded files are passed to preprocessing.

------------------------------------------------------------------------

## US-02 --- Extract Text

**As a** user,\
**I want** the system to extract text from my document,\
**so that** the content can be analyzed.

### Acceptance Criteria

-   [ ] Image preprocessing is applied.
-   [ ] An OCR engine is selected.
-   [ ] Extracted text is displayed.
-   [ ] OCR confidence is recorded.

------------------------------------------------------------------------

## US-03 --- Find Similar Documents

**As a** user,\
**I want** the system to find similar documents,\
**so that** I can understand which existing documents are potentially
related.

### Acceptance Criteria

-   [ ] SBERT embedding is generated.
-   [ ] Repository documents are compared.
-   [ ] Top-k candidates are returned.
-   [ ] Similarity scores are displayed.

------------------------------------------------------------------------

## US-04 --- Detect Plagiarism

**As a** faculty member,\
**I want** the system to identify direct and paraphrased similarity,\
**so that** potentially plagiarized content can be investigated.

### Acceptance Criteria

-   [ ] Lexical similarity is calculated.
-   [ ] Semantic similarity is calculated.
-   [ ] Cross-Encoder similarity is calculated.
-   [ ] Hybrid similarity is generated.

------------------------------------------------------------------------

## US-05 --- View Final Report

**As a** user,\
**I want** to see a final plagiarism score and supporting similarity
information,\
**so that** I can understand the analysis.

### Acceptance Criteria

-   [ ] Final score is displayed.
-   [ ] Similar documents are listed.
-   [ ] Component similarity scores are available.
-   [ ] OCR confidence is shown.

------------------------------------------------------------------------

# 12. Functional Requirements

  ID      Requirement                          Priority
  ------- ------------------------------------ -------------
  FR-01   Upload supported document images     Must Have
  FR-02   Validate uploaded files              Must Have
  FR-03   Preprocess document images           Must Have
  FR-04   Run adaptive OCR                     Must Have
  FR-05   Record OCR confidence                Must Have
  FR-06   Normalize extracted text             Must Have
  FR-07   Generate SBERT embeddings            Must Have
  FR-08   Retrieve top-k similar documents     Must Have
  FR-09   Calculate TF-IDF similarity          Must Have
  FR-10   Calculate semantic similarity        Must Have
  FR-11   Calculate Cross-Encoder similarity   Must Have
  FR-12   Generate hybrid similarity           Must Have
  FR-13   Generate final plagiarism score      Must Have
  FR-14   Display analysis results             Must Have
  FR-15   Store evaluation results             Should Have
  FR-16   Visualization dashboard              Should Have
  FR-17   Detailed report export               Could Have
  FR-18   Multilingual support                 Future

------------------------------------------------------------------------

# 13. Non-Functional Requirements

## 13.1 Performance

-   The system should minimize unnecessary processing by retrieving
    top-k candidate documents before detailed comparison.
-   Processing time should be measured during evaluation.
-   Large document repositories should be considered during performance
    testing.

## 13.2 Reliability

-   OCR failures should be handled gracefully.
-   Invalid documents should generate clear error messages.
-   Similarity calculations should not fail silently.

## 13.3 Usability

-   The upload workflow should be simple.
-   Results should be understandable.
-   Similar documents should be clearly displayed.

## 13.4 Maintainability

-   OCR, preprocessing, retrieval, similarity, and scoring should be
    implemented as separate modules.
-   Models and configuration should be replaceable without rewriting the
    entire application.

## 13.5 Security

-   Uploaded documents should be handled securely.
-   Temporary files should be controlled and removed when no longer
    required.
-   Access to stored academic documents should be restricted according
    to the application's deployment model.

------------------------------------------------------------------------

# 14. Technical Requirements

## 14.1 Software

-   Windows 10/11 or Ubuntu 20.04+
-   Python 3.10+
-   Visual Studio Code / PyCharm / Jupyter Notebook
-   Git

## 14.2 Hardware

-   Intel Core i5 8th Gen or above
-   Minimum 8 GB RAM
-   Approximately 50 GB free storage

## 14.3 Python Libraries

-   OpenCV
-   NumPy
-   Pandas
-   Pillow
-   Tesseract OCR
-   EasyOCR
-   Transformers
-   Sentence-Transformers
-   Scikit-learn
-   PyTorch
-   Matplotlib
-   Seaborn

------------------------------------------------------------------------

# 15. Data Requirements

## 15.1 Dataset Categories

The dataset should contain:

1.  Original handwritten notes.
2.  Paraphrased handwritten notes.
3.  Plagiarized handwritten notes.
4.  Scanned/printed documents where applicable.

The project synopsis identifies publicly available handwriting datasets
such as the **IAM Handwriting Dataset** as a possible source.

## 15.2 Dataset Metadata

Each document should ideally have:

  Field                Description
  -------------------- ---------------------------------------
  document_id          Unique document identifier
  image_path           Location of document image
  original_text        Ground-truth text where available
  extracted_text       OCR output
  document_type        Handwritten / Scanned / Printed
  plagiarism_label     Ground-truth evaluation label
  source_document_id   Related source document if applicable
  language             Document language if recorded

------------------------------------------------------------------------

# 16. Evaluation Strategy

## 16.1 OCR Evaluation

Measure OCR performance against available ground-truth text.

Possible evaluation outputs:

-   OCR Accuracy
-   Character-level/text-level comparison
-   OCR confidence
-   Processing time

## 16.2 Plagiarism Evaluation

Evaluate:

-   Precision
-   Recall
-   F1-score
-   Accuracy
-   Cosine similarity
-   Final plagiarism score
-   Processing time

## 16.3 Comparative Evaluation

Compare:

``` text
Baseline / Existing Method
          VS
Proposed Hybrid Framework
```

The comparison should use the same evaluation dataset and clearly
documented experimental conditions.

------------------------------------------------------------------------

# 17. Project Phases

## Phase 1 --- Research and Planning

**Activities** - Literature review. - Problem definition. - Requirement
analysis. - Architecture design.

**Deliverable** - Approved project architecture and plan.

------------------------------------------------------------------------

## Phase 2 --- Dataset Preparation

**Activities** - Collect handwriting/scanned documents. - Organize
original, paraphrased, and plagiarized samples. - Create metadata. -
Split data for development and evaluation.

**Deliverable** - Prepared dataset.

------------------------------------------------------------------------

## Phase 3 --- Image Preprocessing

**Activities** - Grayscale conversion. - Noise removal. -
Binarization. - Skew correction. - Contrast enhancement.

**Deliverable** - OCR-ready images.

------------------------------------------------------------------------

## Phase 4 --- Adaptive OCR

**Activities** - Integrate Tesseract. - Integrate EasyOCR. - Integrate
TrOCR. - Compare OCR outputs. - Record confidence. - Implement adaptive
selection logic.

**Deliverable** - OCR pipeline.

------------------------------------------------------------------------

## Phase 5 --- Semantic Retrieval

**Activities** - Text preprocessing. - SBERT embedding generation. -
Document embeddings. - Cosine similarity. - Top-k retrieval.

**Deliverable** - Semantic retrieval module.

------------------------------------------------------------------------

## Phase 6 --- Hybrid Plagiarism Detection

**Activities** - TF-IDF implementation. - Lexical cosine similarity. -
SBERT semantic similarity. - Cross-Encoder similarity. - Hybrid score
calculation.

**Deliverable** - Plagiarism detection engine.

------------------------------------------------------------------------

## Phase 7 --- Final Scoring

**Activities** - Combine OCR confidence and similarity scores. -
Experiment with weighting strategies. - Generate final plagiarism
score. - Generate supporting evidence.

**Deliverable** - Final scoring module.

------------------------------------------------------------------------

## Phase 8 --- Evaluation and Application

**Activities** - Evaluate OCR. - Evaluate plagiarism detection. -
Measure processing time. - Build result interface. - Perform integration
testing. - Documentation and presentation.

**Deliverable** - Complete project prototype.

------------------------------------------------------------------------

# 18. Suggested Project Architecture

``` text
project/
│
├── data/
│   ├── raw/
│   ├── processed/
│   ├── documents/
│   └── metadata/
│
├── preprocessing/
│   ├── grayscale.py
│   ├── denoise.py
│   ├── threshold.py
│   └── deskew.py
│
├── ocr/
│   ├── tesseract_engine.py
│   ├── easyocr_engine.py
│   ├── trocr_engine.py
│   └── adaptive_ocr.py
│
├── nlp/
│   ├── text_preprocessing.py
│   ├── sbert_embeddings.py
│   └── retrieval.py
│
├── plagiarism/
│   ├── tfidf_similarity.py
│   ├── semantic_similarity.py
│   ├── cross_encoder.py
│   ├── hybrid_score.py
│   └── final_score.py
│
├── evaluation/
│   ├── ocr_metrics.py
│   ├── plagiarism_metrics.py
│   └── benchmark.py
│
├── app/
│   ├── frontend/
│   └── backend/
│
├── models/
│
├── notebooks/
│
├── tests/
│
├── requirements.txt
├── README.md
└── PRD.md
```

------------------------------------------------------------------------

# 19. Result Dashboard Requirements

The final interface should provide:

### Document Information

-   Uploaded document.
-   Document type.
-   Selected OCR engine.

### OCR Results

-   Extracted text.
-   OCR confidence.
-   Preprocessed image preview.

### Similarity Results

  Candidate      Lexical   Semantic   Contextual   Overall
  ------------ --------- ---------- ------------ ---------
  Document 1         ---        ---          ---       ---
  Document 2         ---        ---          ---       ---
  Document 3         ---        ---          ---       ---

### Final Result

``` text
Final Plagiarism Score: XX%

OCR Confidence: XX%

Potentially Similar Documents: X
```

The actual score presentation and thresholds should be finalized after
experimentation and evaluation.

------------------------------------------------------------------------

# 20. Error and Edge Cases

  Scenario                 Expected Behavior
  ------------------------ -----------------------------------------------
  Unsupported file         Display validation error
  Very low-quality image   Warn user and attempt preprocessing
  OCR fails                Try configured fallback OCR engine
  Empty OCR output         Request clearer document
  No similar documents     Display no significant candidates found
  Very large document      Process within defined limits
  Complex layout           Attempt processing and report OCR limitations
  Model unavailable        Display system error and log failure
  Repository unavailable   Report retrieval failure

------------------------------------------------------------------------

# 21. Risks and Mitigation

  -----------------------------------------------------------------------
  Risk                    Impact                  Mitigation
  ----------------------- ----------------------- -----------------------
  Poor handwriting        High                    Preprocessing + TrOCR

  Low image quality       High                    Denoising +
                                                  thresholding + contrast
                                                  enhancement

  OCR errors              High                    Adaptive OCR +
                                                  confidence tracking

  Paraphrased plagiarism  High                    SBERT + Cross-Encoder

  Large repository        Medium                  Top-k semantic
                                                  retrieval

  High processing time    Medium                  Candidate filtering and
                                                  benchmarking

  Dataset imbalance       Medium                  Balanced evaluation
                                                  data where feasible

  Incorrect scoring       High                    Experimental validation
  weights                                         
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# 22. Dependencies

### Software Dependencies

-   Python 3.10+
-   OpenCV
-   PyTorch
-   Transformers
-   Sentence-Transformers
-   Scikit-learn
-   OCR engines

### Data Dependencies

-   Handwritten document dataset.
-   Original documents.
-   Paraphrased documents.
-   Plagiarized documents.
-   Ground-truth text where available.

### Model Dependencies

-   TrOCR or equivalent handwritten OCR model.
-   Sentence-BERT model.
-   Cross-Encoder model.

------------------------------------------------------------------------

# 23. Out of Scope for Initial Version

The following features are not required for the initial prototype:

-   Full multilingual support.
-   Cloud-scale deployment.
-   Institution-wide production deployment.
-   Automatic legal/disciplinary decisions based on plagiarism scores.
-   Guaranteed detection of every form of plagiarism.
-   Fully automated human-independent academic misconduct decisions.

The system should present similarity evidence and scores as analytical
outputs requiring appropriate interpretation.

------------------------------------------------------------------------

# 24. Success Criteria

The project will be considered successfully implemented when:

-   [ ] Users can upload supported document images.
-   [ ] Document preprocessing works.
-   [ ] At least the planned OCR engines can be integrated/tested.
-   [ ] Text and OCR confidence can be extracted.
-   [ ] SBERT embeddings can be generated.
-   [ ] Top-k similar documents can be retrieved.
-   [ ] TF-IDF similarity works.
-   [ ] Semantic similarity works.
-   [ ] Cross-Encoder similarity works.
-   [ ] Hybrid similarity can be calculated.
-   [ ] Final plagiarism scoring is implemented.
-   [ ] Evaluation metrics are generated.
-   [ ] Complete workflow works from input to final result.
-   [ ] Results can be demonstrated through an application interface.

------------------------------------------------------------------------

# 25. Project Timeline

  Weeks    Activity
  -------- -------------------------------------------
  1--2     Literature Review & Research Planning
  3--4     Dataset Collection & Environment Setup
  5--6     Image Preprocessing & OCR Development
  7--8     Sentence-BERT Semantic Retrieval
  9--10    Hybrid Plagiarism Detection
  11--12   OCR Confidence & Final Plagiarism Score
  13--14   Model Evaluation & Performance Comparison
  15       Documentation & Report Writing
  16       Final Review & Presentation

------------------------------------------------------------------------

# 26. MVP Definition

The **Minimum Viable Product (MVP)** should contain:

``` text
Upload Image
     ↓
Preprocess Image
     ↓
TrOCR / OCR
     ↓
Extract Text
     ↓
SBERT Embedding
     ↓
Retrieve Similar Documents
     ↓
TF-IDF + SBERT + Cross-Encoder
     ↓
Hybrid Score
     ↓
Final Plagiarism Result
```

### MVP Deliverables

1.  Working document upload.
2.  Working preprocessing pipeline.
3.  Working OCR.
4.  Working semantic retrieval.
5.  Working hybrid plagiarism detection.
6.  Working final score.
7.  Basic results dashboard.
8.  Evaluation report.

------------------------------------------------------------------------

# 27. Future Enhancements

Potential future versions can include:

-   Multilingual OCR.
-   Multilingual semantic embeddings.
-   Cloud deployment.
-   Vector database integration.
-   Large-scale document indexing.
-   Document/PDF batch processing.
-   Sentence-level plagiarism highlighting.
-   Side-by-side source comparison.
-   Detailed downloadable reports.
-   User authentication and role management.
-   Institution-specific document repositories.
-   Improved adaptive model selection.

------------------------------------------------------------------------

# 28. Key Technical Decisions to Finalize During Development

The following should remain configurable until experimentation is
complete:

1.  Exact OCR selection criteria.
2.  SBERT model variant.
3.  Cross-Encoder model variant.
4.  Number of top-k retrieval candidates.
5.  Hybrid similarity weights.
6.  Final plagiarism score formula.
7.  Thresholds for displaying similarity categories.
8.  Repository/indexing technology.
9.  Application framework.
10. Deployment architecture.

These decisions should be documented in the technical design document
after benchmarking.

------------------------------------------------------------------------

# 29. Definition of Done

A module is considered complete when:

-   [ ] Code is implemented.
-   [ ] Unit/basic functional tests pass.
-   [ ] Input and output formats are documented.
-   [ ] Error handling is implemented.
-   [ ] Results can be reproduced.
-   [ ] Module is integrated with the next pipeline stage.
-   [ ] Evaluation results are recorded.

The overall project is complete when the full pipeline operates from
**document upload to final plagiarism analysis** and the system has been
evaluated using the defined metrics.

------------------------------------------------------------------------

# 30. References from Project Synopsis

The project synopsis references research covering semantic plagiarism
detection, handwritten OCR, image-based plagiarism detection, SBERT,
BERT/RoBERTa, TrOCR, and related approaches.

Key referenced technologies include:

-   Sentence-BERT for semantic retrieval.
-   TrOCR for handwritten text recognition.
-   Tesseract OCR.
-   TF-IDF and cosine similarity.
-   Cross-Encoder contextual similarity.
-   Image preprocessing techniques.

------------------------------------------------------------------------

# 31. Summary

The **Intelligent Adaptive OCR and Hybrid Semantic Similarity
Framework** combines computer vision, OCR, NLP, and semantic similarity
into one plagiarism detection pipeline.

The core idea is:

> **Improve the document → Read the document → Understand the document →
> Compare the document → Generate a plagiarism score.**

The project is divided into eight major implementation phases:

**Research → Dataset → Preprocessing → Adaptive OCR → Semantic Retrieval
→ Hybrid Detection → Final Scoring → Evaluation & Application**

This phased architecture allows the team to develop and test each
component independently before integrating the complete system.
