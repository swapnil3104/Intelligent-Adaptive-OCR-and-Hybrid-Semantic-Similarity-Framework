# Architecture --- Intelligent Adaptive OCR and Hybrid Semantic Similarity Framework

> **Project:** Intelligent Adaptive OCR and Hybrid Semantic Similarity
> Framework\
> **Architecture Version:** 1.0\
> **Project Type:** Final Year B.Tech CSE Mega Project\
> **Architecture Style:** Modular AI/NLP Pipeline\
> **Primary Domain:** Handwritten, Scanned, and Printed Document
> Plagiarism Detection

------------------------------------------------------------------------

## 1. Architecture Overview

The proposed system is a modular document-analysis pipeline that
combines:

-   Image preprocessing
-   Adaptive OCR
-   Text preprocessing
-   Semantic document retrieval
-   Lexical similarity
-   Semantic similarity
-   Contextual similarity
-   Hybrid plagiarism scoring
-   Evaluation and reporting

The core architecture follows:

``` text
Document
   ↓
Image Preprocessing
   ↓
Adaptive OCR
   ↓
Extracted Text + OCR Confidence
   ↓
Text Preprocessing
   ↓
SBERT Embedding
   ↓
Top-K Similar Document Retrieval
   ↓
┌─────────────────────────────────────────────┐
│          Hybrid Similarity Analysis         │
│                                             │
│  TF-IDF + Cosine  |  SBERT  | Cross-Encoder│
└─────────────────────────────────────────────┘
   ↓
Hybrid Similarity
   ↓
OCR Confidence + Similarity Scores
   ↓
Weighted Final Plagiarism Score
   ↓
Results / Evaluation
```

The project synopsis specifies image preprocessing, adaptive selection
among Tesseract/EasyOCR/TrOCR, SBERT-based retrieval, TF-IDF/cosine
similarity, Cross-Encoder analysis, and weighted final scoring as the
proposed methodology.

------------------------------------------------------------------------

# 2. High-Level System Architecture

``` mermaid
flowchart TD
    A[User / Faculty / Student] --> B[Document Upload]

    B --> C[Input Validation]
    C --> D[Image Preprocessing]

    D --> D1[Grayscale]
    D --> D2[Noise Removal]
    D --> D3[Binarization]
    D --> D4[Skew Correction]
    D --> D5[Contrast Enhancement]

    D --> E[Adaptive OCR Layer]

    E --> E1[Tesseract OCR]
    E --> E2[EasyOCR]
    E --> E3[TrOCR]

    E --> F[OCR Selection / Output]
    F --> G[Extracted Text + OCR Confidence]

    G --> H[Text Preprocessing]
    H --> H1[Lowercasing]
    H --> H2[Tokenization]
    H --> H3[Stop-word Removal]
    H --> H4[Lemmatization]

    H --> I[SBERT Embedding]
    I --> J[Semantic Retrieval]
    J --> K[Top-K Similar Documents]

    K --> L[Hybrid Plagiarism Analysis]

    L --> L1[TF-IDF + Cosine Similarity]
    L --> L2[SBERT Semantic Similarity]
    L --> L3[Cross-Encoder Similarity]

    L1 --> M[Hybrid Scoring]
    L2 --> M
    L3 --> M

    G --> N[OCR Confidence]
    N --> O[Final Weighted Score]
    M --> O

    O --> P[Plagiarism Result]
    P --> Q[Evaluation / Dashboard]
```

------------------------------------------------------------------------

# 3. Architectural Layers

The system is divided into the following logical layers:

``` text
┌─────────────────────────────────────────────┐
│              Presentation Layer             │
│       Upload / Results / Visualization      │
├─────────────────────────────────────────────┤
│             Application Layer               │
│       Pipeline Orchestration / APIs         │
├─────────────────────────────────────────────┤
│              AI Processing Layer            │
│ OCR / SBERT / Cross-Encoder / Scoring       │
├─────────────────────────────────────────────┤
│             NLP Processing Layer             │
│ Text Cleaning / TF-IDF / Embeddings         │
├─────────────────────────────────────────────┤
│          Computer Vision Layer              │
│ Image Enhancement / Preprocessing            │
├─────────────────────────────────────────────┤
│             Data & Repository Layer         │
│ Documents / Metadata / Embeddings           │
└─────────────────────────────────────────────┘
```

------------------------------------------------------------------------

# 4. Layer 1 --- Presentation Layer

## Purpose

Provides the interface through which users upload documents and view
plagiarism analysis results.

## Responsibilities

-   Document upload
-   File validation feedback
-   Processing status
-   Extracted text display
-   OCR engine display
-   OCR confidence display
-   Similar document display
-   Similarity scores
-   Final plagiarism score
-   Evaluation visualizations

## Example UI

``` text
+------------------------------------------------+
|       Intelligent Plagiarism Detection         |
+------------------------------------------------+
|                                                |
|  Upload Document                               |
|  [ Choose File ]                               |
|                                                |
|  Document Type: [Auto Detect]                  |
|                                                |
|             [ Analyze Document ]               |
|                                                |
+------------------------------------------------+

                 Processing...

+------------------------------------------------+
| OCR Results                                    |
| Engine: TrOCR                                  |
| Confidence: XX%                                |
|                                                |
| Extracted Text:                                |
| ---------------------------------------------  |
| ...                                            |
+------------------------------------------------+

+------------------------------------------------+
| Similar Documents                              |
|                                                |
| Document 1      XX%                            |
| Document 2      XX%                            |
| Document 3      XX%                            |
+------------------------------------------------+

+------------------------------------------------+
| Final Plagiarism Score: XX%                    |
+------------------------------------------------+
```

------------------------------------------------------------------------

# 5. Layer 2 --- Application / Orchestration Layer

## Purpose

Coordinates the complete document-processing workflow.

## Responsibilities

1.  Receive uploaded document.
2.  Validate input.
3.  Start preprocessing.
4.  Invoke adaptive OCR.
5.  Store extracted text and confidence.
6.  Start text preprocessing.
7.  Generate SBERT embeddings.
8.  Retrieve top-k candidate documents.
9.  Run hybrid similarity analysis.
10. Calculate final score.
11. Return results.

## Pipeline Controller

``` text
Upload
  ↓
Validate
  ↓
Preprocess
  ↓
OCR
  ↓
Text Processing
  ↓
Semantic Retrieval
  ↓
Similarity Analysis
  ↓
Final Scoring
  ↓
Result
```

------------------------------------------------------------------------

# 6. Layer 3 --- Computer Vision / Image Processing

## Purpose

Improve document quality before OCR.

## Input

``` text
Raw Handwritten / Scanned / Printed Image
```

## Processing

``` mermaid
flowchart LR
    A[Raw Image] --> B[Grayscale]
    B --> C[Noise Removal]
    C --> D[Binarization]
    D --> E[Skew Correction]
    E --> F[Contrast Enhancement]
    F --> G[OCR Ready Image]
```

## Components

### 6.1 Grayscale Conversion

Converts a color image into grayscale representation.

### 6.2 Noise Removal

Reduces unwanted image noise that can affect OCR.

### 6.3 Binarization

Separates foreground text from the background.

### 6.4 Skew Correction

Corrects rotated or tilted documents.

### 6.5 Contrast Enhancement

Improves the visibility of text.

------------------------------------------------------------------------

# 7. Layer 4 --- Adaptive OCR Layer

## Purpose

Extract text from the processed document using an appropriate OCR
engine.

The proposed framework includes:

``` text
                OCR Router
                   │
       ┌───────────┼───────────┐
       ↓           ↓           ↓
  Tesseract     EasyOCR      TrOCR
       │           │           │
       └───────────┼───────────┘
                   ↓
        Extracted Text + Confidence
```

## OCR Engines

  Engine      Intended Role
  ----------- ------------------------------
  Tesseract   Printed text recognition
  EasyOCR     Complex image-based text
  TrOCR       Handwritten text recognition

## OCR Output

``` json
{
  "text": "extracted document content",
  "engine": "TrOCR",
  "confidence": 0.00
}
```

The exact confidence representation depends on the selected OCR
implementation.

------------------------------------------------------------------------

# 8. Adaptive OCR Decision Layer

The architecture should allow the OCR selection mechanism to evolve
during experimentation.

Conceptually:

``` text
Input Image
    ↓
Image Quality / Document Characteristics
    ↓
OCR Selection
    ├── Printed → Tesseract
    ├── Complex Image → EasyOCR
    └── Handwritten → TrOCR
    ↓
OCR Result
```

### Important Design Principle

The final selection rules should be based on experimental evaluation
rather than hard-coded assumptions.

------------------------------------------------------------------------

# 9. Layer 5 --- Text Processing

## Purpose

Normalize OCR output before similarity analysis.

## Pipeline

``` mermaid
flowchart LR
    A[OCR Text] --> B[Lowercase]
    B --> C[Punctuation Removal]
    C --> D[Tokenization]
    D --> E[Stop-word Removal]
    E --> F[Lemmatization]
    F --> G[Clean Text]
```

## Output

``` text
Raw OCR Text
       ↓
Normalized Text
       ↓
Similarity Processing
```

------------------------------------------------------------------------

# 10. Layer 6 --- Semantic Retrieval

## Purpose

Reduce the search space by finding the most relevant documents from the
repository.

## Technology

**Sentence-BERT (SBERT)**

## Architecture

``` text
Clean Extracted Text
        ↓
   SBERT Encoder
        ↓
Document Embedding
        ↓
Compare with Repository Embeddings
        ↓
Cosine Similarity
        ↓
Rank Documents
        ↓
Top-K Candidates
```

## Example

``` text
Input Document
      ↓
Embedding: [0.12, 0.81, ...]
      ↓
┌────────────────────────────┐
│ Document Repository        │
│                            │
│ Doc-001 → similarity       │
│ Doc-002 → similarity       │
│ Doc-003 → similarity       │
│ ...                        │
└────────────────────────────┘
      ↓
Top-K Documents
```

------------------------------------------------------------------------

# 11. Document Repository Architecture

The repository contains the documents against which the uploaded
document is compared.

``` text
Document Repository
│
├── Original Documents
├── Paraphrased Documents
├── Plagiarized Documents
├── Scanned Documents
├── Handwritten Documents
└── Printed Documents
```

Each document should ideally have metadata such as:

  Field                Purpose
  -------------------- -----------------------------------
  document_id          Unique identifier
  image_path           Source image
  original_text        Ground-truth text where available
  extracted_text       OCR output
  document_type        Handwritten / Scanned / Printed
  plagiarism_label     Evaluation label
  source_document_id   Related source
  embedding            Semantic representation

------------------------------------------------------------------------

# 12. Embedding Pipeline

A document embedding pipeline can be represented as:

``` mermaid
flowchart TD
    A[Document Text] --> B[Text Preprocessing]
    B --> C[Sentence-BERT]
    C --> D[Dense Vector]
    D --> E[Similarity Search]
```

The same embedding process should be used consistently for query
documents and repository documents when performing semantic retrieval.

------------------------------------------------------------------------

# 13. Layer 7 --- Hybrid Plagiarism Detection

This is the central analysis layer.

It combines three complementary signals:

``` text
                  Candidate Document
                         │
          ┌──────────────┼──────────────┐
          ↓              ↓              ↓
       TF-IDF          SBERT       Cross-Encoder
          ↓              ↓              ↓
     Lexical Score   Semantic Score  Contextual Score
          └──────────────┼──────────────┘
                         ↓
                  Hybrid Score
```

------------------------------------------------------------------------

# 14. Lexical Similarity Module

## Technology

-   TF-IDF
-   Cosine Similarity

## Purpose

Measure similarity based on lexical/term-level information.

``` text
Document A
    ↓
TF-IDF Vector

Document B
    ↓
TF-IDF Vector

      ↓

Cosine Similarity
      ↓
Lexical Similarity Score
```

------------------------------------------------------------------------

# 15. Semantic Similarity Module

## Technology

-   Sentence-BERT
-   Cosine Similarity

## Purpose

Measure similarity based on semantic meaning rather than only exact word
overlap.

``` text
Document A → SBERT → Vector A
                         │
                         ├── Cosine Similarity
                         │
Document B → SBERT → Vector B
                         ↓
                 Semantic Score
```

------------------------------------------------------------------------

# 16. Contextual Similarity Module

## Technology

-   Cross-Encoder
-   MiniLM/BERT-based model

## Purpose

Perform contextual pairwise comparison between candidate document
content.

``` text
Text A + Text B
      ↓
Cross-Encoder
      ↓
Contextual Similarity Score
```

The exact Cross-Encoder model should be selected during experimentation
and documented in the implementation.

------------------------------------------------------------------------

# 17. Hybrid Scoring Architecture

The three similarity signals are combined:

``` mermaid
flowchart TD
    A[Candidate Document] --> B[TF-IDF]
    A --> C[SBERT]
    A --> D[Cross-Encoder]

    B --> E[Lexical Similarity]
    C --> F[Semantic Similarity]
    D --> G[Contextual Similarity]

    E --> H[Hybrid Scoring]
    F --> H
    G --> H

    H --> I[Hybrid Similarity Score]
```

The weighting values should be determined experimentally.

------------------------------------------------------------------------

# 18. Final Plagiarism Scoring Architecture

The final score combines:

1.  OCR confidence.
2.  Lexical similarity.
3.  Semantic similarity.
4.  Contextual similarity.

``` mermaid
flowchart TD
    A[OCR Confidence] --> E[Weighted Scoring]
    B[Lexical Similarity] --> E
    C[Semantic Similarity] --> E
    D[Cross-Encoder Similarity] --> E

    E --> F[Final Plagiarism Score]
    F --> G[Result Dashboard]
```

## Conceptual Formula

``` text
Final Score =
    f(
       OCR Confidence,
       Lexical Similarity,
       Semantic Similarity,
       Contextual Similarity
    )
```

A concrete formula and weights should be established only after
experimental validation.

------------------------------------------------------------------------

# 19. End-to-End Architecture

``` mermaid
flowchart TB
    U[User] --> UI[Web / Application Interface]

    UI --> API[Application Controller]

    API --> PRE[Image Preprocessing]

    PRE --> OCR[Adaptive OCR]

    OCR --> TXT[Extracted Text]
    OCR --> CONF[OCR Confidence]

    TXT --> NLP[Text Preprocessing]

    NLP --> SBERT[SBERT Encoder]

    SBERT --> RET[Semantic Retrieval]

    RET --> CAND[Top-K Candidate Documents]

    CAND --> TF[TF-IDF + Cosine]
    CAND --> SEM[SBERT Similarity]
    CAND --> CE[Cross-Encoder]

    TF --> HYB[Hybrid Similarity]
    SEM --> HYB
    CE --> HYB

    CONF --> SCORE[Final Weighted Scoring]
    HYB --> SCORE

    SCORE --> RESULT[Plagiarism Result]
    RESULT --> UI

    REPO[(Document Repository)] --> RET
    REPO --> TF
    REPO --> SEM
    REPO --> CE
```

------------------------------------------------------------------------

# 20. Data Flow

## Level 0 --- Context

``` text
             ┌─────────────────────┐
             │        USER         │
             └──────────┬──────────┘
                        │
                        │ Document
                        ↓
        ┌───────────────────────────────┐
        │ Intelligent Plagiarism       │
        │ Detection Framework           │
        └───────────────┬───────────────┘
                        │
                        │ Results
                        ↓
             ┌─────────────────────┐
             │        USER         │
             └─────────────────────┘
```

------------------------------------------------------------------------

# 21. Data Flow --- Level 1

``` text
Document
   ↓
[1] Preprocessing
   ↓
Processed Image
   ↓
[2] Adaptive OCR
   ↓
Text + OCR Confidence
   ↓
[3] Text Processing
   ↓
Clean Text
   ↓
[4] SBERT Retrieval
   ↓
Top-K Candidates
   ↓
[5] Hybrid Analysis
   ↓
Similarity Scores
   ↓
[6] Final Scoring
   ↓
Final Plagiarism Score
```

------------------------------------------------------------------------

# 22. Component Architecture

``` text
┌──────────────────────────────────────────────────────┐
│                 APPLICATION                         │
│                                                    │
│  Upload API │ Processing API │ Result API          │
└───────────────────────┬──────────────────────────────┘
                        │
                        ↓
┌──────────────────────────────────────────────────────┐
│              DOCUMENT PROCESSING                     │
│                                                    │
│  Validation │ Preprocessing │ OCR                  │
└───────────────────────┬──────────────────────────────┘
                        │
                        ↓
┌──────────────────────────────────────────────────────┐
│                 NLP ENGINE                          │
│                                                    │
│ Text Cleaning │ TF-IDF │ SBERT │ Cross-Encoder    │
└───────────────────────┬──────────────────────────────┘
                        │
                        ↓
┌──────────────────────────────────────────────────────┐
│                 SCORING ENGINE                      │
│                                                    │
│ Hybrid Similarity │ OCR Confidence │ Final Score   │
└───────────────────────┬──────────────────────────────┘
                        │
                        ↓
┌──────────────────────────────────────────────────────┐
│                  DATA LAYER                          │
│                                                    │
│ Documents │ Metadata │ Embeddings │ Results        │
└──────────────────────────────────────────────────────┘
```

------------------------------------------------------------------------

# 23. Suggested Backend Structure

``` text
backend/
│
├── api/
│   ├── upload.py
│   ├── analysis.py
│   └── results.py
│
├── preprocessing/
│   ├── image_processor.py
│   ├── denoise.py
│   ├── threshold.py
│   └── deskew.py
│
├── ocr/
│   ├── base.py
│   ├── tesseract.py
│   ├── easyocr.py
│   ├── trocr.py
│   └── adaptive.py
│
├── nlp/
│   ├── preprocess.py
│   ├── sbert.py
│   └── retrieval.py
│
├── plagiarism/
│   ├── tfidf.py
│   ├── semantic.py
│   ├── cross_encoder.py
│   ├── hybrid.py
│   └── scoring.py
│
├── evaluation/
│   ├── ocr_metrics.py
│   ├── classification_metrics.py
│   └── benchmark.py
│
├── models/
│
├── repository/
│
└── config/
```

------------------------------------------------------------------------

# 24. Suggested Frontend Structure

``` text
frontend/
│
├── pages/
│   ├── Home
│   ├── Upload
│   ├── Processing
│   └── Results
│
├── components/
│   ├── UploadBox
│   ├── OCRResult
│   ├── SimilarDocuments
│   ├── SimilarityTable
│   ├── ScoreCard
│   └── ProcessingStatus
│
├── services/
│   └── api.js
│
└── utils/
```

The specific frontend framework is intentionally left open because the
project synopsis specifies the Python/AI stack but does not mandate a
particular frontend framework.

------------------------------------------------------------------------

# 25. Data Storage Architecture

A logical storage design can contain:

``` text
                    DATA LAYER
                        │
        ┌───────────────┼────────────────┐
        ↓               ↓                ↓
   Documents        Metadata         Embeddings
        │               │                │
        └───────────────┼────────────────┘
                        ↓
                   Results
```

## Documents

Stores original or processed document files.

## Metadata

Stores:

-   Document ID
-   Type
-   Source
-   Labels
-   Processing information

## Embeddings

Stores SBERT representations for semantic retrieval.

## Results

Stores:

-   OCR engine
-   OCR confidence
-   Candidate documents
-   Similarity scores
-   Final score
-   Processing time

------------------------------------------------------------------------

# 26. Model Architecture

## 26.1 OCR Models

``` text
                  OCR Layer
                     │
       ┌─────────────┼─────────────┐
       ↓             ↓             ↓
  Tesseract       EasyOCR        TrOCR
       │             │             │
       └─────────────┼─────────────┘
                     ↓
              Extracted Text
```

------------------------------------------------------------------------

## 26.2 SBERT

``` text
Input Text
    ↓
Tokenizer
    ↓
Transformer Encoder
    ↓
Sentence Representation
    ↓
Embedding Vector
```

Used for semantic retrieval and semantic similarity.

------------------------------------------------------------------------

## 26.3 Cross-Encoder

``` text
Document A + Document B
          ↓
      Tokenizer
          ↓
    Transformer
          ↓
 Contextual Score
```

Used for detailed candidate-pair comparison.

------------------------------------------------------------------------

# 27. Retrieval Architecture

The system should separate **candidate retrieval** from **detailed
plagiarism analysis**.

``` text
                Document Repository
                        │
                        ↓
                  SBERT Embeddings
                        │
                        ↓
                  Similarity Search
                        │
                        ↓
                     Top-K
                        │
                        ↓
              Detailed Analysis Only
                        │
          ┌─────────────┼─────────────┐
          ↓             ↓             ↓
        TF-IDF        SBERT      Cross-Encoder
```

This architecture prevents every uploaded document from necessarily
going through every expensive comparison step.

------------------------------------------------------------------------

# 28. Processing States

The application should expose clear processing states:

``` text
UPLOADED
   ↓
VALIDATED
   ↓
PREPROCESSING
   ↓
OCR_PROCESSING
   ↓
TEXT_READY
   ↓
EMBEDDING
   ↓
RETRIEVING
   ↓
SIMILARITY_ANALYSIS
   ↓
SCORING
   ↓
COMPLETED
```

Failure states can occur at any stage:

``` text
ANY STAGE
   ↓
FAILED
   ↓
Error Message + Diagnostic Information
```

------------------------------------------------------------------------

# 29. Error Handling Architecture

``` text
Input
  ↓
Validation
  ├── Invalid → Validation Error
  └── Valid
        ↓
Preprocessing
  ├── Failed → Processing Error
  └── Success
        ↓
OCR
  ├── Failed → OCR Error / Fallback
  └── Success
        ↓
Retrieval
  ├── Failed → Retrieval Error
  └── Success
        ↓
Similarity
  ├── Failed → Analysis Error
  └── Success
        ↓
Result
```

------------------------------------------------------------------------

# 30. Evaluation Architecture

Evaluation should be performed at multiple levels.

``` mermaid
flowchart TD
    A[Test Dataset] --> B[OCR Evaluation]
    A --> C[Retrieval Evaluation]
    A --> D[Plagiarism Evaluation]
    A --> E[Performance Evaluation]

    B --> B1[OCR Accuracy]
    C --> C1[Cosine Similarity / Retrieval Results]
    D --> D1[Precision]
    D --> D2[Recall]
    D --> D3[F1-Score]
    D --> D4[Accuracy]
    E --> E1[Processing Time]

    B1 --> F[Evaluation Report]
    C1 --> F
    D1 --> F
    D2 --> F
    D3 --> F
    D4 --> F
    E1 --> F
```

------------------------------------------------------------------------

# 31. Security and Privacy Architecture

Since academic documents may contain private information, the
application should follow a controlled document-handling model.

``` text
User Upload
    ↓
Input Validation
    ↓
Controlled Temporary Storage
    ↓
Processing
    ↓
Result Generation
    ↓
Controlled Result Storage
```

Recommended principles:

-   Validate uploaded files.
-   Restrict access to stored documents.
-   Avoid unnecessary long-term storage of temporary files.
-   Keep model outputs associated with the correct document ID.
-   Do not expose repository documents to unauthorized users.

------------------------------------------------------------------------

# 32. Performance Architecture

The main performance optimization is **candidate filtering**.

### Without Retrieval

``` text
Uploaded Document
       ↓
Compare against every document
       ↓
Detailed similarity analysis
```

### Proposed Architecture

``` text
Uploaded Document
       ↓
SBERT Retrieval
       ↓
Top-K Candidates
       ↓
Detailed Hybrid Analysis
```

The top-k value should be configurable and evaluated experimentally.

------------------------------------------------------------------------

# 33. Deployment Architecture

A simple deployment model can be:

``` text
             User Browser
                  │
                  ↓
          Frontend Application
                  │
                  ↓
             Backend API
                  │
       ┌──────────┼──────────┐
       ↓          ↓          ↓
 Image/OCR     NLP/AI     Repository
 Processing    Models       Data
       │          │          │
       └──────────┼──────────┘
                  ↓
             Final Result
```

For the initial academic prototype, local deployment is sufficient.
Cloud deployment can be considered as future scope.

------------------------------------------------------------------------

# 34. Complete Technical Stack

  Layer                   Proposed Technology
  ----------------------- -------------------------------
  Programming             Python 3.10+
  Image Processing        OpenCV, Pillow
  OCR                     Tesseract, EasyOCR, TrOCR
  Numerical Processing    NumPy
  Data Processing         Pandas
  NLP                     Transformers
  Semantic Embeddings     Sentence-Transformers / SBERT
  Lexical Similarity      Scikit-learn TF-IDF
  Similarity              Cosine Similarity
  Contextual Similarity   Cross-Encoder
  Deep Learning           PyTorch
  Visualization           Matplotlib / Seaborn
  Version Control         Git
  Development             VS Code / PyCharm / Jupyter

------------------------------------------------------------------------

# 35. Architecture-to-Project-Phase Mapping

  Phase     Architecture Components
  --------- -----------------------------------------------
  Phase 1   Requirements, architecture, literature review
  Phase 2   Dataset and repository
  Phase 3   Image preprocessing
  Phase 4   Adaptive OCR
  Phase 5   Text processing + SBERT retrieval
  Phase 6   TF-IDF + SBERT + Cross-Encoder
  Phase 7   Hybrid and final scoring
  Phase 8   Evaluation + application + deployment

------------------------------------------------------------------------

# 36. End-to-End Example

Suppose a student uploads a handwritten assignment.

``` text
Step 1
Student uploads image
        ↓
Step 2
OpenCV improves image quality
        ↓
Step 3
Adaptive OCR selects TrOCR
        ↓
Step 4
Text + OCR confidence generated
        ↓
Step 5
Text is normalized
        ↓
Step 6
SBERT creates document embedding
        ↓
Step 7
Top-k similar documents retrieved
        ↓
Step 8
Each candidate is analyzed using:
        ├── TF-IDF
        ├── SBERT
        └── Cross-Encoder
        ↓
Step 9
Hybrid similarity calculated
        ↓
Step 10
OCR confidence + similarity signals
are combined
        ↓
Step 11
Final plagiarism score generated
        ↓
Step 12
Results displayed to user
```

------------------------------------------------------------------------

# 37. Architecture Principles

The implementation should follow these principles:

### 1. Modularity

Each major component should be independently replaceable.

### 2. Separation of Concerns

OCR, retrieval, similarity, scoring, and UI should not be tightly
coupled.

### 3. Experiment-Driven Configuration

Model choices, weights, thresholds, and top-k values should be
configurable.

### 4. Reproducibility

Evaluation experiments should record model versions, configuration,
dataset split, and metrics.

### 5. Explainability

The result should expose supporting similarity signals rather than only
displaying a single final score.

### 6. Extensibility

The architecture should allow additional OCR engines, embedding models,
languages, and retrieval technologies to be added later.

------------------------------------------------------------------------

# 38. Key Architectural Decisions

  Decision              Current Direction
  --------------------- --------------------------------------------
  Input                 Handwritten, scanned, printed images
  Preprocessing         OpenCV-based
  OCR                   Adaptive Tesseract/EasyOCR/TrOCR
  Text Processing       Standard NLP normalization
  Retrieval             SBERT + cosine similarity
  Lexical Analysis      TF-IDF + cosine
  Semantic Analysis     SBERT
  Contextual Analysis   Cross-Encoder
  Final Scoring         Weighted combination
  Evaluation            OCR + classification + similarity + timing
  Deployment            Local prototype initially
  Multilingual          Future scope

------------------------------------------------------------------------

# 39. Architecture Limitations

The architecture inherits several limitations identified in the project
synopsis:

-   OCR may still degrade with poor handwriting or low-quality images.
-   Complex layouts may reduce extraction quality.
-   Advanced OCR and similarity models may increase processing time.
-   The quality of plagiarism detection depends on the document
    repository and evaluation dataset.
-   The final scoring weights require experimental validation.
-   Multilingual support is not part of the initial implementation.

------------------------------------------------------------------------

# 40. Final Architecture Summary

The proposed architecture can be summarized as:

``` text
                  ┌──────────────────────┐
                  │        USER          │
                  └──────────┬───────────┘
                             ↓
                  ┌──────────────────────┐
                  │  DOCUMENT UPLOAD     │
                  └──────────┬───────────┘
                             ↓
                  ┌──────────────────────┐
                  │ IMAGE PREPROCESSING  │
                  └──────────┬───────────┘
                             ↓
                  ┌──────────────────────┐
                  │    ADAPTIVE OCR      │
                  │ Tesseract/EasyOCR/   │
                  │       TrOCR          │
                  └──────────┬───────────┘
                             ↓
                  ┌──────────────────────┐
                  │ TEXT + OCR CONFIDENCE│
                  └──────────┬───────────┘
                             ↓
                  ┌──────────────────────┐
                  │  TEXT PREPROCESSING  │
                  └──────────┬───────────┘
                             ↓
                  ┌──────────────────────┐
                  │       SBERT          │
                  │ SEMANTIC EMBEDDINGS  │
                  └──────────┬───────────┘
                             ↓
                  ┌──────────────────────┐
                  │   TOP-K RETRIEVAL    │
                  └──────────┬───────────┘
                             ↓
              ┌──────────────┼──────────────┐
              ↓              ↓              ↓
        ┌──────────┐   ┌──────────┐   ┌────────────┐
        │  TF-IDF  │   │  SBERT   │   │Cross-Encoder│
        │ Similarity│   │Similarity│   │ Similarity │
        └─────┬────┘   └────┬─────┘   └──────┬─────┘
              └──────────────┼───────────────┘
                             ↓
                  ┌──────────────────────┐
                  │  HYBRID SIMILARITY   │
                  └──────────┬───────────┘
                             ↓
                  ┌──────────────────────┐
                  │ OCR + SIMILARITY     │
                  │ WEIGHTED SCORING     │
                  └──────────┬───────────┘
                             ↓
                  ┌──────────────────────┐
                  │ FINAL PLAGIARISM     │
                  │       SCORE          │
                  └──────────┬───────────┘
                             ↓
                  ┌──────────────────────┐
                  │ RESULT + EVALUATION  │
                  └──────────────────────┘
```

> **Core architectural idea:**\
> **Computer Vision reads the document → OCR converts it to text → NLP
> understands the text → Retrieval finds candidates → Hybrid similarity
> detects plagiarism → Scoring produces the final analytical result.**
