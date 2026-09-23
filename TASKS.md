# TASKS.md

# Development Task Plan --- Intelligent Adaptive OCR and Hybrid Semantic Similarity Framework

> This file converts the approved project modules and architecture into
> an implementation-ready task plan for an AI coding agent.
>
> Tasks follow the project's development order and preserve the core
> pipeline:
>
> **Document → Image Preprocessing → Adaptive OCR → Text Processing →
> SBERT Retrieval → TF-IDF + SBERT + Cross-Encoder → Hybrid Similarity →
> Final Scoring → Evaluation → UI**

------------------------------------------------------------------------

# 1. Task Management Rules

Use this file as the master development backlog.

Each task should:

-   Have a unique ID.
-   Belong to a project phase/module.
-   Declare dependencies where applicable.
-   Have clear acceptance criteria.
-   Be completed and tested before dependent work begins.
-   Never introduce an undocumented architectural change.

Recommended task status values:

``` text
pending
in-progress
in-review
completed
blocked
cancelled
```

Recommended priority:

``` text
critical
high
medium
low
```

Recommended effort:

``` text
small
medium
large
```

------------------------------------------------------------------------

# 2. Project Module Map

``` text
M00 Project Foundation
 │
 ├── M01 Dataset & Data Management
 │
 ├── M02 Image Preprocessing
 │
 ├── M03 OCR Engine Integration
 │
 ├── M04 Adaptive OCR
 │
 ├── M05 Text Preprocessing
 │
 ├── M06 SBERT Semantic Retrieval
 │
 ├── M07 Lexical Similarity — TF-IDF
 │
 ├── M08 Semantic Similarity — SBERT
 │
 ├── M09 Contextual Similarity — Cross-Encoder
 │
 ├── M10 Hybrid Similarity
 │
 ├── M11 Final Scoring
 │
 ├── M12 End-to-End Pipeline
 │
 ├── M13 Evaluation & Experiments
 │
 ├── M14 Backend/API
 │
 ├── M15 Frontend/UI
 │
 ├── M16 Integration & Testing
 │
 └── M17 Documentation & Deployment
```

------------------------------------------------------------------------

# 3. Development Dependency Graph

``` text
M00
 ↓
M01
 ↓
M02
 ↓
M03
 ↓
M04
 ↓
M05
 ↓
M06 ─────────────┐
 ↓               │
M07             │
 ↓               │
M08             ├──→ M10 → M11
 ↓               │          ↓
M09 ─────────────┘          ↓
                            M12
                             ↓
                       M13 / M14 / M15
                             ↓
                            M16
                             ↓
                            M17
```

Some tasks can be developed in parallel once their dependencies are
satisfied.

------------------------------------------------------------------------

# 4. M00 --- Project Foundation

## TASK-001 --- Create Project Repository

**Priority:** critical\
**Effort:** small\
**Dependencies:** none

### Objective

Create the base repository structure.

### Tasks

-   [ ] Create Git repository.
-   [ ] Create `main` and development branch.
-   [ ] Add `.gitignore`.
-   [ ] Add `README.md`.
-   [ ] Add `PRD.md`.
-   [ ] Add `architecture.md`.
-   [ ] Add `DEVELOPMENT_RULES.md`.
-   [ ] Add `DESIGN.md`.
-   [ ] Add `TASKS.md`.

### Suggested structure

``` text
project/
├── docs/
├── src/
├── tests/
├── data/
├── configs/
├── scripts/
├── notebooks/
├── requirements.txt
├── .gitignore
└── README.md
```

### Acceptance Criteria

-   Repository is initialized.
-   Documentation files are present.
-   No generated secrets or datasets are committed.

------------------------------------------------------------------------

## TASK-002 --- Configure Python Environment

**Priority:** critical\
**Effort:** small\
**Dependencies:** `TASK-001`

### Tasks

-   [ ] Create Python virtual environment.
-   [ ] Configure Python 3.10+.
-   [ ] Add core dependencies.
-   [ ] Generate `requirements.txt`.
-   [ ] Verify imports.
-   [ ] Document installation commands.

### Acceptance Criteria

A clean environment can install the project dependencies successfully.

------------------------------------------------------------------------

## TASK-003 --- Create Configuration System

**Priority:** high\
**Effort:** medium\
**Dependencies:** `TASK-002`

### Tasks

-   [ ] Create application configuration.
-   [ ] Create model configuration.
-   [ ] Create OCR configuration.
-   [ ] Create scoring configuration.
-   [ ] Create dataset paths.
-   [ ] Create environment-specific configuration where required.

### Acceptance Criteria

Models, paths, top-k, thresholds, and scoring weights are configurable
rather than scattered through source code.

------------------------------------------------------------------------

# 5. M01 --- Dataset & Data Management

## TASK-004 --- Define Dataset Structure

**Priority:** critical\
**Effort:** small\
**Dependencies:** `TASK-001`

### Structure

``` text
data/
├── raw/
├── processed/
├── metadata/
├── repository/
└── evaluation/
```

### Tasks

-   [ ] Define supported document formats.
-   [ ] Define metadata schema.
-   [ ] Define document IDs.
-   [ ] Define evaluation labels where available.
-   [ ] Define train/development/evaluation separation.

### Acceptance Criteria

Raw data can be stored without being overwritten by preprocessing.

------------------------------------------------------------------------

## TASK-005 --- Build Dataset Loader

**Priority:** high\
**Effort:** medium\
**Dependencies:** `TASK-004`

### Tasks

-   [ ] Implement image/document discovery.
-   [ ] Read metadata.
-   [ ] Validate files.
-   [ ] Generate document IDs.
-   [ ] Return standardized dataset objects.

### Acceptance Criteria

The loader can reliably iterate through valid project documents and
reject invalid inputs.

------------------------------------------------------------------------

## TASK-006 --- Create Ground-Truth Management

**Priority:** high\
**Effort:** medium\
**Dependencies:** `TASK-004`

### Tasks

-   [ ] Define ground-truth format.
-   [ ] Keep ground truth separate from predictions.
-   [ ] Validate labels.
-   [ ] Prevent evaluation data leakage.

### Acceptance Criteria

Ground-truth data cannot be accidentally replaced by model output.

------------------------------------------------------------------------

# 6. M02 --- Image Preprocessing

## TASK-007 --- Implement Grayscale Conversion

**Priority:** high\
**Effort:** small\
**Dependencies:** `TASK-005`

### Acceptance Criteria

-   [ ] Valid images are converted.
-   [ ] Invalid images raise clear errors.
-   [ ] Original images remain unchanged.
-   [ ] Unit tests pass.

------------------------------------------------------------------------

## TASK-008 --- Implement Noise Removal

**Priority:** high\
**Effort:** small\
**Dependencies:** `TASK-007`

### Tasks

-   [ ] Select appropriate denoising method.
-   [ ] Make parameters configurable.
-   [ ] Compare output visually on sample documents.

------------------------------------------------------------------------

## TASK-009 --- Implement Binarization

**Priority:** high\
**Effort:** medium\
**Dependencies:** `TASK-007`

### Tasks

-   [ ] Implement thresholding.
-   [ ] Support configurable parameters.
-   [ ] Test handwritten and printed samples.

------------------------------------------------------------------------

## TASK-010 --- Implement Deskew

**Priority:** high\
**Effort:** medium\
**Dependencies:** `TASK-009`

### Tasks

-   [ ] Detect document skew.
-   [ ] Correct rotation.
-   [ ] Handle already aligned documents.

------------------------------------------------------------------------

## TASK-011 --- Implement Contrast Enhancement

**Priority:** medium\
**Effort:** small\
**Dependencies:** `TASK-007`

### Tasks

-   [ ] Implement contrast enhancement.
-   [ ] Make enhancement optional.
-   [ ] Compare OCR performance with and without enhancement.

------------------------------------------------------------------------

## TASK-012 --- Build Image Processing Pipeline

**Priority:** critical\
**Effort:** medium\
**Dependencies:** `TASK-008`, `TASK-009`, `TASK-010`, `TASK-011`

### Pipeline

``` text
Input
 ↓
Grayscale
 ↓
Denoise
 ↓
Binarize
 ↓
Deskew
 ↓
Contrast Enhancement
 ↓
Output
```

### Acceptance Criteria

A single preprocessing service can execute the configured sequence and
return the processed document without modifying the raw input.

------------------------------------------------------------------------

# 7. M03 --- OCR Engine Integration

## TASK-013 --- Define OCR Interface

**Priority:** critical\
**Effort:** small\
**Dependencies:** `TASK-012`

### Output contract

``` python
{
    "text": "...",
    "engine": "...",
    "confidence": 0.0
}
```

### Acceptance Criteria

All OCR engines can conform to the same interface.

------------------------------------------------------------------------

## TASK-014 --- Integrate Tesseract OCR

**Priority:** high\
**Effort:** medium\
**Dependencies:** `TASK-013`

### Tasks

-   [ ] Configure Tesseract.
-   [ ] Implement text extraction.
-   [ ] Capture confidence where supported.
-   [ ] Handle OCR failures.
-   [ ] Add tests.

------------------------------------------------------------------------

## TASK-015 --- Integrate EasyOCR

**Priority:** high\
**Effort:** medium\
**Dependencies:** `TASK-013`

### Tasks

-   [ ] Initialize EasyOCR.
-   [ ] Extract text.
-   [ ] Aggregate recognition results.
-   [ ] Handle errors.
-   [ ] Add tests.

------------------------------------------------------------------------

## TASK-016 --- Integrate TrOCR

**Priority:** high\
**Effort:** large\
**Dependencies:** `TASK-013`

### Tasks

-   [ ] Load processor.
-   [ ] Load model.
-   [ ] Configure CPU/GPU.
-   [ ] Extract text.
-   [ ] Handle model loading errors.
-   [ ] Measure processing time.

### Acceptance Criteria

TrOCR can process supported document images through the common OCR
interface.

------------------------------------------------------------------------

# 8. M04 --- Adaptive OCR

## TASK-017 --- Define OCR Selection Criteria

**Priority:** high\
**Effort:** medium\
**Dependencies:** `TASK-014`, `TASK-015`, `TASK-016`

### Possible inputs

-   Image quality
-   Document type
-   Preprocessing result
-   OCR confidence
-   Processing constraints

### Important

Do not claim that one OCR engine is better without experimental
evidence.

------------------------------------------------------------------------

## TASK-018 --- Implement Adaptive OCR Orchestrator

**Priority:** critical\
**Effort:** large\
**Dependencies:** `TASK-017`

### Pipeline

``` text
Image
 ↓
Document Characteristics
 ↓
OCR Selection
 ↓
Selected Engine
 ↓
Text + Confidence
```

### Acceptance Criteria

The orchestrator can select/configure an OCR engine using documented
logic and return a standardized OCR result.

------------------------------------------------------------------------

## TASK-019 --- Compare OCR Engines

**Priority:** high\
**Effort:** medium\
**Dependencies:** `TASK-018`

### Metrics

-   OCR accuracy where ground truth exists.
-   OCR confidence.
-   Processing time.

### Acceptance Criteria

A reproducible comparison report is generated without fabricating
metrics.

------------------------------------------------------------------------

# 9. M05 --- Text Preprocessing

## TASK-020 --- Preserve Raw OCR Output

**Priority:** critical\
**Effort:** small\
**Dependencies:** `TASK-018`

### Acceptance Criteria

The original OCR text remains available after cleaning.

------------------------------------------------------------------------

## TASK-021 --- Implement Text Normalization

**Priority:** high\
**Effort:** medium\
**Dependencies:** `TASK-020`

### Pipeline

``` text
Raw OCR
 ↓
Lowercase
 ↓
Punctuation Removal
 ↓
Tokenization
 ↓
Stop-word Removal
 ↓
Lemmatization
 ↓
Clean Text
```

------------------------------------------------------------------------

## TASK-022 --- Validate Text Preprocessing

**Priority:** high\
**Effort:** small\
**Dependencies:** `TASK-021`

### Tests

-   [ ] Empty text.
-   [ ] Very short text.
-   [ ] Punctuation-heavy text.
-   [ ] OCR noise.
-   [ ] Normal text.

------------------------------------------------------------------------

# 10. M06 --- SBERT Semantic Retrieval

## TASK-023 --- Select Configurable SBERT Model

**Priority:** high\
**Effort:** small\
**Dependencies:** `TASK-022`

### Tasks

-   [ ] Configure model name.
-   [ ] Record model version.
-   [ ] Record embedding dimension.
-   [ ] Support CPU/GPU.

------------------------------------------------------------------------

## TASK-024 --- Implement Document Embedding

**Priority:** critical\
**Effort:** medium\
**Dependencies:** `TASK-023`

### Acceptance Criteria

Clean document text can be transformed into a deterministic embedding
under a fixed model/configuration.

------------------------------------------------------------------------

## TASK-025 --- Build Repository Embedding Index

**Priority:** critical\
**Effort:** large\
**Dependencies:** `TASK-024`, `TASK-005`

### Pipeline

``` text
Repository Documents
 ↓
Text Preprocessing
 ↓
SBERT
 ↓
Embeddings
 ↓
Repository Index
```

### Acceptance Criteria

Repository embeddings are generated separately and can be reused across
analysis requests.

------------------------------------------------------------------------

## TASK-026 --- Implement Top-K Retrieval

**Priority:** critical\
**Effort:** medium\
**Dependencies:** `TASK-025`

### Pipeline

``` text
Query Document
 ↓
SBERT Embedding
 ↓
Similarity Search
 ↓
Top-K Candidates
```

### Acceptance Criteria

The system returns ranked candidate documents with actual similarity
values.

------------------------------------------------------------------------

# 11. M07 --- TF-IDF Lexical Similarity

## TASK-027 --- Implement TF-IDF Vectorization

**Priority:** high\
**Effort:** medium\
**Dependencies:** `TASK-022`, `TASK-026`

### Acceptance Criteria

The system can generate TF-IDF representations for the query and
candidate documents.

------------------------------------------------------------------------

## TASK-028 --- Implement Cosine Similarity

**Priority:** high\
**Effort:** small\
**Dependencies:** `TASK-027`

### Acceptance Criteria

The system returns lexical similarity scores for document pairs.

------------------------------------------------------------------------

## TASK-029 --- Test Lexical Similarity

**Priority:** medium\
**Effort:** small\
**Dependencies:** `TASK-028`

### Test Cases

-   Identical documents.
-   Completely different documents.
-   Partially overlapping documents.
-   Empty documents.

------------------------------------------------------------------------

# 12. M08 --- SBERT Semantic Similarity

## TASK-030 --- Implement Pairwise SBERT Similarity

**Priority:** high\
**Effort:** medium\
**Dependencies:** `TASK-024`, `TASK-026`

### Pipeline

``` text
Document A
 ↓
Embedding A

Document B
 ↓
Embedding B

A + B
 ↓
Cosine Similarity
```

------------------------------------------------------------------------

## TASK-031 --- Expose Semantic Similarity Score

**Priority:** medium\
**Effort:** small\
**Dependencies:** `TASK-030`

Return:

``` json
{
  "semantic_similarity": 0.0
}
```

The value must come from actual model inference.

------------------------------------------------------------------------

# 13. M09 --- Cross-Encoder Contextual Similarity

## TASK-032 --- Integrate Cross-Encoder

**Priority:** high\
**Effort:** large\
**Dependencies:** `TASK-026`, `TASK-022`

### Tasks

-   [ ] Configure model.
-   [ ] Load model once.
-   [ ] Process candidate pairs.
-   [ ] Capture scores.
-   [ ] Handle model errors.

------------------------------------------------------------------------

## TASK-033 --- Implement Pairwise Contextual Analysis

**Priority:** high\
**Effort:** medium\
**Dependencies:** `TASK-032`

### Acceptance Criteria

The system can calculate contextual similarity for retrieved candidate
pairs.

------------------------------------------------------------------------

# 14. M10 --- Hybrid Similarity

## TASK-034 --- Define Hybrid Similarity Contract

**Priority:** critical\
**Effort:** small\
**Dependencies:** `TASK-029`, `TASK-031`, `TASK-033`

### Output

``` json
{
  "lexical_similarity": 0.0,
  "semantic_similarity": 0.0,
  "contextual_similarity": 0.0,
  "hybrid_similarity": 0.0
}
```

------------------------------------------------------------------------

## TASK-035 --- Implement Hybrid Similarity Calculation

**Priority:** critical\
**Effort:** medium\
**Dependencies:** `TASK-034`

### Concept

``` text
TF-IDF
   +
SBERT
   +
Cross-Encoder
   ↓
Hybrid Similarity
```

### Important

Weights must be configurable and experimentally justified.

------------------------------------------------------------------------

## TASK-036 --- Compare Individual vs Hybrid Methods

**Priority:** high\
**Effort:** medium\
**Dependencies:** `TASK-035`

### Compare

``` text
TF-IDF
SBERT
Cross-Encoder
Hybrid
```

Do not declare a superior method without evaluation.

------------------------------------------------------------------------

# 15. M11 --- Final Scoring

## TASK-037 --- Define Final Score Configuration

**Priority:** critical\
**Effort:** medium\
**Dependencies:** `TASK-035`

### Inputs

``` text
OCR Confidence
Lexical Similarity
Semantic Similarity
Contextual Similarity
```

### Requirement

The exact mathematical formula and weights must be documented before
implementation.

------------------------------------------------------------------------

## TASK-038 --- Implement Final Score

**Priority:** critical\
**Effort:** medium\
**Dependencies:** `TASK-037`

### Acceptance Criteria

The final score:

-   Uses actual pipeline outputs.
-   Uses configurable weights.
-   Is reproducible.
-   Exposes component scores.

------------------------------------------------------------------------

## TASK-039 --- Implement Score Explanation

**Priority:** high\
**Effort:** medium\
**Dependencies:** `TASK-038`

### Output

``` text
Final Score
OCR Confidence
Lexical Similarity
Semantic Similarity
Contextual Similarity
```

The result must be interpretable rather than a single unexplained
number.

------------------------------------------------------------------------

# 16. M12 --- End-to-End Pipeline

## TASK-040 --- Build Analysis Orchestrator

**Priority:** critical\
**Effort:** large\
**Dependencies:** `TASK-012`, `TASK-018`, `TASK-021`, `TASK-026`,
`TASK-035`, `TASK-038`

### Pipeline

``` text
Document
 ↓
Preprocessing
 ↓
Adaptive OCR
 ↓
Text Processing
 ↓
SBERT Retrieval
 ↓
Top-K Candidates
 ↓
TF-IDF
 ↓
SBERT Similarity
 ↓
Cross-Encoder
 ↓
Hybrid Similarity
 ↓
Final Score
 ↓
Result
```

------------------------------------------------------------------------

## TASK-041 --- Add Pipeline Timing

**Priority:** medium\
**Effort:** small\
**Dependencies:** `TASK-040`

Track:

``` text
Preprocessing Time
OCR Time
Text Processing Time
Retrieval Time
TF-IDF Time
SBERT Time
Cross-Encoder Time
Total Time
```

Only report measured values.

------------------------------------------------------------------------

## TASK-042 --- Add Pipeline Error Handling

**Priority:** high\
**Effort:** medium\
**Dependencies:** `TASK-040`

### Acceptance Criteria

A failure in one stage produces a meaningful error and does not silently
return fabricated results.

------------------------------------------------------------------------

# 17. M13 --- Evaluation & Experiments

## TASK-043 --- Create Experiment Schema

**Priority:** high\
**Effort:** medium\
**Dependencies:** `TASK-040`

Record:

``` text
Experiment ID
Date
Dataset
OCR Engine
OCR Model
SBERT Model
Cross-Encoder
Preprocessing
Top-K
Weights
Metrics
Hardware
Processing Time
Notes
```

------------------------------------------------------------------------

## TASK-044 --- OCR Evaluation

**Priority:** high\
**Effort:** medium\
**Dependencies:** `TASK-019`

### Evaluate

-   OCR accuracy where ground truth exists.
-   OCR confidence.
-   Processing time.

------------------------------------------------------------------------

## TASK-045 --- Retrieval Evaluation

**Priority:** high\
**Effort:** medium\
**Dependencies:** `TASK-026`

Evaluate retrieval quality using the available ground truth.

Do not invent retrieval metrics when ground truth is unavailable.

------------------------------------------------------------------------

## TASK-046 --- Similarity Evaluation

**Priority:** high\
**Effort:** medium\
**Dependencies:** `TASK-036`

Compare:

``` text
TF-IDF
SBERT
Cross-Encoder
Hybrid
```

------------------------------------------------------------------------

## TASK-047 --- Final Scoring Evaluation

**Priority:** high\
**Effort:** medium\
**Dependencies:** `TASK-039`

Evaluate final scoring against the project's defined evaluation labels.

------------------------------------------------------------------------

## TASK-048 --- Experiment Reproducibility

**Priority:** medium\
**Effort:** medium\
**Dependencies:** `TASK-043`

Verify that an experiment can be recreated from:

``` text
Dataset
+
Configuration
+
Model versions
+
Code version
```

------------------------------------------------------------------------

# 18. M14 --- Backend/API

## TASK-049 --- Design Backend API

**Priority:** high\
**Effort:** medium\
**Dependencies:** `TASK-040`

Potential endpoints:

``` text
POST /api/upload
POST /api/analyze
GET  /api/results/{id}
GET  /api/documents/{id}
GET  /api/health
```

The final API contract must match actual backend implementation.

------------------------------------------------------------------------

## TASK-050 --- Implement Upload API

**Priority:** high\
**Effort:** medium\
**Dependencies:** `TASK-049`

### Requirements

-   Validate file.
-   Store safely.
-   Generate document ID.
-   Return upload status.

------------------------------------------------------------------------

## TASK-051 --- Implement Analysis API

**Priority:** critical\
**Effort:** large\
**Dependencies:** `TASK-050`, `TASK-040`

### Acceptance Criteria

The API can submit a document to the analysis pipeline and return a real
analysis result.

------------------------------------------------------------------------

## TASK-052 --- Implement Result API

**Priority:** high\
**Effort:** medium\
**Dependencies:** `TASK-051`

Return:

``` text
OCR Result
Similarity Results
Candidate Documents
Score Breakdown
Final Score
Timing
```

------------------------------------------------------------------------

# 19. M15 --- Frontend/UI

## TASK-053 --- Create Frontend Foundation

**Priority:** high\
**Effort:** medium\
**Dependencies:** `TASK-049`

### Tasks

-   [ ] Create frontend project.
-   [ ] Add routing.
-   [ ] Add design tokens.
-   [ ] Add layout.
-   [ ] Add responsive structure.

------------------------------------------------------------------------

## TASK-054 --- Build Dashboard

**Priority:** medium\
**Effort:** medium\
**Dependencies:** `TASK-053`

Include:

-   Project introduction.
-   Capabilities.
-   Analyze button.
-   Optional aggregate metrics.

------------------------------------------------------------------------

## TASK-055 --- Build Document Upload UI

**Priority:** critical\
**Effort:** medium\
**Dependencies:** `TASK-053`, `TASK-050`

Include:

-   Drag-and-drop.
-   Browse file.
-   Preview.
-   Validation.
-   Upload status.

------------------------------------------------------------------------

## TASK-056 --- Build Processing UI

**Priority:** high\
**Effort:** medium\
**Dependencies:** `TASK-055`, `TASK-051`

Display:

``` text
Preprocessing
OCR
Text Processing
Retrieval
Similarity
Scoring
```

Use actual backend status where available.

------------------------------------------------------------------------

## TASK-057 --- Build OCR Results UI

**Priority:** high\
**Effort:** medium\
**Dependencies:** `TASK-052`

Display:

-   Extracted text.
-   OCR engine.
-   OCR confidence.
-   Processing time.

------------------------------------------------------------------------

## TASK-058 --- Build Similarity Results UI

**Priority:** critical\
**Effort:** medium\
**Dependencies:** `TASK-052`

Display:

-   Final score.
-   Similar documents.
-   Lexical similarity.
-   Semantic similarity.
-   Contextual similarity.
-   Hybrid score.

------------------------------------------------------------------------

## TASK-059 --- Build Detailed Comparison UI

**Priority:** high\
**Effort:** large\
**Dependencies:** `TASK-058`

Allow the user to inspect document evidence and similarity information.

------------------------------------------------------------------------

## TASK-060 --- Build Evaluation Dashboard

**Priority:** medium\
**Effort:** medium\
**Dependencies:** `TASK-044`, `TASK-045`, `TASK-046`, `TASK-047`

Display only actual experiment results.

------------------------------------------------------------------------

# 20. M16 --- Integration & Testing

## TASK-061 --- Unit Test Image Pipeline

**Priority:** high\
**Effort:** medium\
**Dependencies:** `TASK-012`

------------------------------------------------------------------------

## TASK-062 --- Unit Test OCR Pipeline

**Priority:** high\
**Effort:** medium\
**Dependencies:** `TASK-018`

------------------------------------------------------------------------

## TASK-063 --- Unit Test Retrieval

**Priority:** high\
**Effort:** medium\
**Dependencies:** `TASK-026`

------------------------------------------------------------------------

## TASK-064 --- Unit Test Similarity Models

**Priority:** high\
**Effort:** medium\
**Dependencies:** `TASK-035`

------------------------------------------------------------------------

## TASK-065 --- Unit Test Scoring

**Priority:** critical\
**Effort:** small\
**Dependencies:** `TASK-038`

------------------------------------------------------------------------

## TASK-066 --- End-to-End Test

**Priority:** critical\
**Effort:** large\
**Dependencies:** `TASK-040`, `TASK-051`, `TASK-058`

### Test

``` text
Upload
 ↓
Preprocess
 ↓
OCR
 ↓
Text
 ↓
Retrieval
 ↓
Hybrid Analysis
 ↓
Final Score
 ↓
UI Result
```

------------------------------------------------------------------------

## TASK-067 --- Error Scenario Testing

**Priority:** high\
**Effort:** medium\
**Dependencies:** `TASK-066`

Test:

-   Invalid image.
-   Empty document.
-   OCR failure.
-   Model unavailable.
-   Repository unavailable.
-   Invalid configuration.
-   Very large file.

------------------------------------------------------------------------

# 21. M17 --- Documentation & Deployment

## TASK-068 --- Update README

**Priority:** high\
**Effort:** medium\
**Dependencies:** `TASK-066`

Include:

-   Project overview.
-   Architecture.
-   Installation.
-   Dataset setup.
-   Running instructions.
-   Evaluation.
-   Limitations.
-   Future scope.

------------------------------------------------------------------------

## TASK-069 --- Document API

**Priority:** medium\
**Effort:** medium\
**Dependencies:** `TASK-052`

Document actual endpoints and schemas.

------------------------------------------------------------------------

## TASK-070 --- Document Research Methodology

**Priority:** high\
**Effort:** medium\
**Dependencies:** `TASK-047`

Document:

``` text
Preprocessing
OCR
Text Processing
Retrieval
Similarity
Scoring
Evaluation
```

------------------------------------------------------------------------

## TASK-071 --- Create Deployment Configuration

**Priority:** medium\
**Effort:** large\
**Dependencies:** `TASK-066`

Deployment should only be implemented after the local end-to-end system
is stable.

------------------------------------------------------------------------

# 22. Final MVP Definition

The MVP is considered complete when these tasks are completed:

``` text
TASK-001
TASK-002
TASK-003
TASK-004
TASK-005
TASK-012
TASK-013
TASK-016
TASK-018
TASK-021
TASK-024
TASK-026
TASK-028
TASK-030
TASK-033
TASK-035
TASK-038
TASK-040
TASK-051
TASK-055
TASK-056
TASK-058
TASK-066
```

The MVP must support:

``` text
Document Upload
      ↓
Image Preprocessing
      ↓
OCR
      ↓
OCR Confidence
      ↓
Text Processing
      ↓
SBERT Retrieval
      ↓
Top-K Candidates
      ↓
TF-IDF
      +
SBERT
      +
Cross-Encoder
      ↓
Hybrid Similarity
      ↓
Final Score
      ↓
Results UI
```

------------------------------------------------------------------------

# 23. Definition of Done

A task is **Done** only when:

``` text
[ ] Implementation completed
[ ] Relevant tests written
[ ] Relevant tests passed
[ ] Error handling considered
[ ] Configuration updated
[ ] Documentation updated where required
[ ] Architecture preserved
[ ] No secrets committed
[ ] No fake results introduced
[ ] No raw data overwritten
```

For research tasks additionally:

``` text
[ ] Experiment configuration recorded
[ ] Dataset/version recorded
[ ] Model/version recorded
[ ] Metrics generated from actual runs
[ ] Results reproducible
```

------------------------------------------------------------------------

# 24. AI Agent Execution Rules

When an AI agent receives a task from this file:

### Step 1

Read:

``` text
PRD.md
architecture.md
DEVELOPMENT_RULES.md
DESIGN.md
```

when relevant.

### Step 2

Check the task's dependencies.

### Step 3

Inspect the existing implementation before modifying it.

### Step 4

Implement the smallest change required.

### Step 5

Run relevant tests.

### Step 6

Check architecture compatibility.

### Step 7

Update documentation/configuration if required.

### Step 8

Report:

``` text
Task completed
Files changed
Tests run
Results
Known limitations
Next available task
```

------------------------------------------------------------------------

# 25. AI Task Selection Rule

When asked:

> "What should I build next?"

select a task that is:

1.  `pending`
2.  Has all dependencies completed
3.  Has high/critical priority where possible
4.  Does not violate module order

Never start a task whose required dependencies are incomplete unless
explicitly instructed.

------------------------------------------------------------------------

# 26. Parallel Development Opportunities

The following can be developed in parallel after their prerequisites are
complete:

``` text
Image preprocessing tests
        │
        ├── OCR engine integration
        │
        └── Dataset tooling
```

After retrieval is stable:

``` text
TF-IDF
SBERT similarity
Cross-Encoder
```

can be implemented as separate modules.

After backend contracts are defined:

``` text
Backend implementation
Frontend components
Evaluation tooling
```

can proceed in parallel where practical.

------------------------------------------------------------------------

# 27. Important Research Rules

The task system must preserve these principles:

### Never fabricate results

Do not mark a model as successful until it has been evaluated.

### Never modify ground truth

Ground truth is an evaluation asset.

### Never confuse OCR confidence with plagiarism

They measure different things.

### Never call retrieval proof of plagiarism

Retrieval identifies candidate documents.

### Never claim hybrid scoring is better without comparison

The hybrid approach must be evaluated against appropriate baselines.

### Never hard-code experimental conclusions

Configuration and results must remain reproducible.

------------------------------------------------------------------------

# 28. Suggested Development Milestones

## Milestone 1 --- Foundation

``` text
TASK-001 → TASK-006
```

Deliverable:

``` text
Working repository + dataset infrastructure
```

------------------------------------------------------------------------

## Milestone 2 --- OCR

``` text
TASK-007 → TASK-019
```

Deliverable:

``` text
Preprocessing + OCR + adaptive OCR
```

------------------------------------------------------------------------

## Milestone 3 --- NLP Retrieval

``` text
TASK-020 → TASK-026
```

Deliverable:

``` text
Clean text + SBERT retrieval
```

------------------------------------------------------------------------

## Milestone 4 --- Similarity Engine

``` text
TASK-027 → TASK-039
```

Deliverable:

``` text
TF-IDF + SBERT + Cross-Encoder + Hybrid + Final Score
```

------------------------------------------------------------------------

## Milestone 5 --- End-to-End AI Pipeline

``` text
TASK-040 → TASK-048
```

Deliverable:

``` text
Complete research pipeline + evaluation
```

------------------------------------------------------------------------

## Milestone 6 --- Application

``` text
TASK-049 → TASK-060
```

Deliverable:

``` text
Backend API + Frontend UI
```

------------------------------------------------------------------------

## Milestone 7 --- Production Readiness

``` text
TASK-061 → TASK-071
```

Deliverable:

``` text
Testing + Documentation + Deployment
```

------------------------------------------------------------------------

# 29. Master Progress Tracker

``` text
M00 Project Foundation       ☐
M01 Dataset                  ☐
M02 Image Preprocessing      ☐
M03 OCR Engines              ☐
M04 Adaptive OCR             ☐
M05 Text Processing          ☐
M06 SBERT Retrieval          ☐
M07 TF-IDF                   ☐
M08 SBERT Similarity         ☐
M09 Cross-Encoder            ☐
M10 Hybrid Similarity        ☐
M11 Final Scoring            ☐
M12 End-to-End Pipeline      ☐
M13 Evaluation               ☐
M14 Backend                  ☐
M15 Frontend                 ☐
M16 Testing                  ☐
M17 Documentation/Deployment ☐
```

------------------------------------------------------------------------

# 30. Final Project Workflow

``` text
                    ┌───────────────┐
                    │    Upload     │
                    └───────┬───────┘
                            ↓
                    ┌───────────────┐
                    │ Preprocessing │
                    └───────┬───────┘
                            ↓
                    ┌───────────────┐
                    │ Adaptive OCR  │
                    └───────┬───────┘
                            ↓
                    ┌───────────────┐
                    │ Text Cleaning │
                    └───────┬───────┘
                            ↓
                    ┌───────────────┐
                    │ SBERT Search  │
                    └───────┬───────┘
                            ↓
                    ┌───────────────┐
                    │    Top-K      │
                    └───────┬───────┘
                            ↓
             ┌──────────────┼──────────────┐
             ↓              ↓              ↓
          TF-IDF          SBERT      Cross-Encoder
             └──────────────┼──────────────┘
                            ↓
                    ┌───────────────┐
                    │ Hybrid Score  │
                    └───────┬───────┘
                            ↓
                    ┌───────────────┐
                    │ Final Scoring │
                    └───────┬───────┘
                            ↓
                    ┌───────────────┐
                    │   Results     │
                    └───────┬───────┘
                            ↓
                    ┌───────────────┐
                    │  Evaluation   │
                    └───────────────┘
```

------------------------------------------------------------------------

# 31. Task File Convention

If these tasks are later split into individual taskmd-compatible files,
use:

``` text
tasks/
├── 001-project-repository.md
├── 002-python-environment.md
├── 003-configuration.md
├── 004-dataset-structure.md
├── ...
├── 040-analysis-orchestrator.md
├── ...
└── 071-deployment.md
```

Each task file can use YAML frontmatter such as:

``` yaml
---
id: "001"
title: "Create project repository"
status: pending
priority: critical
effort: small
type: chore
dependencies: []
tags:
  - foundation
  - setup
phase: "M00"
created_at: 2026-09-23
---
```

This follows the documented taskmd convention of YAML frontmatter with
task metadata and a Markdown task body. citeturn0search0turn0search1

------------------------------------------------------------------------

# 32. Final Rule

The AI development agent must treat this task plan as an execution
roadmap, not as permission to change the project methodology.

The expected order is:

``` text
PLAN
 ↓
FOUNDATION
 ↓
DATA
 ↓
PREPROCESSING
 ↓
OCR
 ↓
TEXT
 ↓
RETRIEVAL
 ↓
SIMILARITY
 ↓
SCORING
 ↓
PIPELINE
 ↓
EVALUATION
 ↓
BACKEND
 ↓
FRONTEND
 ↓
TESTING
 ↓
DOCUMENTATION
 ↓
DEPLOYMENT
```

**Build incrementally. Test every module. Preserve the architecture.
Record experiments. Never fabricate results.**
