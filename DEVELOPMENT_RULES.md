# DEVELOPMENT_RULES.md

# AI Development Rules --- Intelligent Adaptive OCR and Hybrid Semantic Similarity Framework

> **Purpose:** This document is the mandatory development guide for any
> AI coding agent, developer assistant, or automated engineering system
> working on this project.
>
> **Primary principle:** Build the system incrementally, preserve the
> approved architecture, avoid unsupported assumptions, and never
> silently change the research methodology.

------------------------------------------------------------------------

# 1. AI ROLE

You are an **AI software development agent** responsible for helping
implement the project:

**Intelligent Adaptive OCR and Hybrid Semantic Similarity Framework**

Your job is to:

-   Understand the approved project requirements.
-   Implement one module at a time.
-   Preserve the defined architecture.
-   Write maintainable, testable, reproducible code.
-   Explain important implementation decisions.
-   Detect inconsistencies before making architectural changes.
-   Ask for clarification when a requirement is genuinely ambiguous.
-   Never invent datasets, metrics, model results, APIs, or experimental
    findings.

You are **not allowed to silently redesign the research methodology**.

------------------------------------------------------------------------

# 2. SOURCE OF TRUTH

Use project documentation in the following priority order:

``` text
1. Project PRD
2. Architecture document
3. Approved project synopsis / methodology
4. Current implementation and tests
5. Developer/user instructions for the current task
6. General technical knowledge
```

When documents conflict:

1.  Do not silently choose one.
2.  Identify the conflict.
3.  Prefer the higher-priority project document.
4.  If the conflict affects architecture or research methodology, ask
    for confirmation before changing it.

The project synopsis defines the core methodology as:

``` text
Document
→ Image Preprocessing
→ Adaptive OCR
→ Extracted Text + OCR Confidence
→ Text Preprocessing
→ SBERT Semantic Retrieval
→ Top-K Candidate Documents
→ TF-IDF + SBERT + Cross-Encoder
→ Hybrid Similarity
→ OCR Confidence + Similarity-Based Scoring
→ Final Plagiarism Score
```

The synopsis explicitly describes preprocessing, adaptive OCR, SBERT
retrieval, lexical similarity, semantic similarity, Cross-Encoder
contextual similarity, and weighted final scoring. Do not replace these
core components without explicit approval.

------------------------------------------------------------------------

# 3. PROJECT OBJECTIVE

The system is intended to analyze:

-   Handwritten documents
-   Scanned documents
-   Printed documents

and support plagiarism analysis through:

-   Image preprocessing
-   Adaptive OCR
-   OCR confidence
-   Text normalization
-   Semantic retrieval
-   Lexical similarity
-   Semantic similarity
-   Contextual similarity
-   Hybrid scoring

The system must be designed to identify both:

``` text
Direct / lexical similarity
+
Paraphrased / semantic similarity
```

------------------------------------------------------------------------

# 4. CORE ARCHITECTURE RULE

The architecture must remain modular.

``` text
Presentation
    ↓
Application / Orchestration
    ↓
Image Processing
    ↓
Adaptive OCR
    ↓
Text Processing
    ↓
Semantic Retrieval
    ↓
Hybrid Plagiarism Detection
    ↓
Final Scoring
    ↓
Results / Evaluation
```

Do not create a monolithic file containing the entire pipeline.

Each major responsibility must have a clear module.

------------------------------------------------------------------------

# 5. MODULE BOUNDARIES

The following boundaries are mandatory.

## 5.1 Image Preprocessing

Responsible only for document-image preparation.

Expected operations:

-   Grayscale conversion
-   Noise removal
-   Binarization
-   Skew correction
-   Contrast enhancement

Do not put plagiarism logic inside image preprocessing.

------------------------------------------------------------------------

## 5.2 OCR

Responsible for text extraction.

Supported OCR engines:

-   Tesseract
-   EasyOCR
-   TrOCR

OCR output should conceptually contain:

``` python
{
    "text": "...",
    "engine": "...",
    "confidence": 0.0
}
```

The exact confidence representation must match the selected OCR
implementation.

Do not fabricate confidence values.

------------------------------------------------------------------------

## 5.3 Adaptive OCR

Adaptive OCR is an orchestration/selection layer.

Conceptually:

``` text
Input Image
    ↓
Document Characteristics / Quality
    ↓
OCR Selection
    ↓
Selected OCR Engine
    ↓
Text + Confidence
```

Do not claim that the system automatically selects the best OCR engine
unless the selection logic has actually been implemented and evaluated.

If the initial version uses a fixed engine such as TrOCR, document that
explicitly.

------------------------------------------------------------------------

## 5.4 Text Preprocessing

Expected operations:

``` text
OCR Text
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

Keep text preprocessing separate from OCR.

Do not destroy the original OCR output.

Always preserve:

``` text
raw_ocr_text
clean_text
```

when practical.

------------------------------------------------------------------------

## 5.5 Semantic Retrieval

Use Sentence-BERT / Sentence-Transformers for semantic embeddings.

Pipeline:

``` text
Clean Text
    ↓
SBERT
    ↓
Embedding
    ↓
Similarity Search
    ↓
Top-K Candidates
```

The retrieval layer should be independent from the detailed plagiarism
analysis layer.

------------------------------------------------------------------------

## 5.6 Lexical Similarity

Use:

-   TF-IDF
-   Cosine similarity

Purpose:

``` text
Measure lexical / term-level similarity.
```

Do not describe lexical similarity as semantic understanding.

------------------------------------------------------------------------

## 5.7 Semantic Similarity

Use:

-   SBERT embeddings
-   Cosine similarity

Purpose:

``` text
Measure semantic similarity between content.
```

Keep SBERT retrieval and SBERT detailed similarity logically
distinguishable even if they reuse the same embedding model.

------------------------------------------------------------------------

## 5.8 Contextual Similarity

Use a Cross-Encoder model.

The architecture allows a MiniLM/BERT-based Cross-Encoder.

The exact model must be configurable.

Do not hard-code a model name everywhere in the application.

------------------------------------------------------------------------

## 5.9 Hybrid Similarity

Combine:

``` text
Lexical Similarity
+
Semantic Similarity
+
Contextual Similarity
```

into a hybrid similarity score.

Do not introduce arbitrary weights without documenting and validating
them.

------------------------------------------------------------------------

## 5.10 Final Plagiarism Score

The final score may combine:

``` text
OCR Confidence
+
Lexical Similarity
+
Semantic Similarity
+
Contextual Similarity
```

The exact mathematical formula and weights must be configurable.

Never claim that a particular weighting is optimal unless experiments
demonstrate it.

------------------------------------------------------------------------

# 6. PHASE-BASED DEVELOPMENT RULE

Development must follow the project phases.

## Phase 1 --- Research and Planning

Tasks:

-   Confirm requirements.
-   Confirm architecture.
-   Set up repository.
-   Set up Python environment.
-   Define coding standards.
-   Define dataset structure.
-   Define evaluation strategy.

Do not begin with a complete application before the processing modules
are understood.

------------------------------------------------------------------------

## Phase 2 --- Dataset Preparation

Tasks:

-   Organize handwritten documents.
-   Organize scanned documents.
-   Organize printed documents.
-   Define metadata.
-   Define ground truth where available.
-   Define plagiarism labels.
-   Create train/development/evaluation splits where appropriate.

Never mix evaluation data into development without documenting it.

------------------------------------------------------------------------

## Phase 3 --- Image Preprocessing

Implement and test:

``` text
grayscale.py
denoise.py
threshold.py
deskew.py
contrast.py
image_processor.py
```

Each transformation should be independently testable.

------------------------------------------------------------------------

## Phase 4 --- Adaptive OCR

Implement:

``` text
ocr/base.py
ocr/tesseract.py
ocr/easyocr.py
ocr/trocr.py
ocr/adaptive.py
```

Start with one working OCR engine before adding orchestration.

Recommended development order:

``` text
TrOCR / selected baseline
      ↓
OCR output validation
      ↓
Confidence extraction
      ↓
Tesseract
      ↓
EasyOCR
      ↓
Adaptive selection
```

Do not implement adaptive routing before individual engines are working.

------------------------------------------------------------------------

## Phase 5 --- Semantic Retrieval

Implement:

``` text
text preprocessing
       ↓
SBERT embeddings
       ↓
repository embeddings
       ↓
cosine similarity
       ↓
top-k retrieval
```

Document:

-   Model name
-   Model version
-   Embedding dimension
-   Similarity method
-   Top-k value

------------------------------------------------------------------------

## Phase 6 --- Hybrid Plagiarism Detection

Implement independently:

``` text
TF-IDF
SBERT similarity
Cross-Encoder
```

Then integrate:

``` text
Hybrid Similarity
```

Do not debug all three models simultaneously.

------------------------------------------------------------------------

## Phase 7 --- Final Scoring

Implement:

``` text
OCR Confidence
      +
Lexical Score
      +
Semantic Score
      +
Contextual Score
      ↓
Weighted Scoring
      ↓
Final Score
```

Weights must be stored in configuration rather than scattered through
source code.

------------------------------------------------------------------------

## Phase 8 --- Evaluation and Application

Only after the core pipeline works:

-   Build the result interface.
-   Add visualizations.
-   Add performance measurements.
-   Run evaluation.
-   Compare configurations.
-   Document results.
-   Prepare demonstration workflow.

------------------------------------------------------------------------

# 7. IMPLEMENTATION ORDER

When starting development from scratch, use this order:

``` text
1. Repository structure
2. Environment setup
3. Configuration system
4. Dataset loader
5. Image preprocessing
6. OCR baseline
7. OCR confidence
8. Text preprocessing
9. SBERT embedding
10. Document retrieval
11. TF-IDF similarity
12. SBERT similarity
13. Cross-Encoder similarity
14. Hybrid score
15. Final score
16. Evaluation
17. Backend/API
18. Frontend/UI
19. Integration tests
20. Documentation
```

Do not skip directly to UI polish while the core research pipeline is
unstable.

------------------------------------------------------------------------

# 8. CODING STYLE

## 8.1 General

Use:

-   Clear names
-   Small functions
-   Single responsibility
-   Type hints where practical
-   Docstrings for public functions/classes
-   Meaningful error messages
-   Constants/configuration instead of magic numbers

Prefer:

``` python
def preprocess_document(image):
    ...
```

over:

``` python
def process(x):
    ...
```

------------------------------------------------------------------------

## 8.2 Naming

Use:

``` text
snake_case
```

for Python functions and variables.

Use:

``` text
PascalCase
```

for classes.

Examples:

``` python
class OCRResult:
    pass

def extract_text(image):
    pass
```

------------------------------------------------------------------------

## 8.3 Comments

Comments should explain:

-   Why a non-obvious decision exists.
-   Why a particular preprocessing step is required.
-   Why a model/configuration was selected.

Do not write comments that simply repeat the code.

Bad:

``` python
# convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
```

Useful:

``` python
# Grayscale simplifies downstream thresholding and reduces
# the input representation to intensity information.
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
```

------------------------------------------------------------------------

# 9. CONFIGURATION RULES

Do not hard-code:

-   Model names
-   OCR engine selection
-   Top-k
-   Similarity thresholds
-   Hybrid weights
-   File paths
-   Dataset paths
-   Device selection
-   Batch size

Use configuration.

Example:

``` yaml
ocr:
  default_engine: trocr

retrieval:
  top_k: 5

scoring:
  lexical_weight: 0.0
  semantic_weight: 0.0
  contextual_weight: 0.0
  ocr_weight: 0.0
```

The values above are placeholders, not approved final weights.

Weights must be experimentally determined.

------------------------------------------------------------------------

# 10. ENVIRONMENT RULES

Use a virtual environment.

Example:

``` bash
python -m venv .venv
```

Activate it before installing dependencies.

Maintain:

``` text
requirements.txt
```

Do not install random dependencies without updating dependency
documentation.

------------------------------------------------------------------------

# 11. DEPENDENCY RULES

The approved project stack includes:

-   Python 3.10+
-   OpenCV
-   NumPy
-   Pandas
-   Pillow
-   Tesseract OCR
-   EasyOCR
-   TrOCR
-   Transformers
-   Sentence-Transformers
-   Scikit-learn
-   PyTorch
-   Matplotlib
-   Seaborn

The project synopsis identifies these technologies as part of the
proposed requirements.

Do not replace a core technology merely because another library is
easier.

If replacement is necessary:

1.  Explain why.
2.  Identify the affected architecture layer.
3.  Identify compatibility implications.
4.  Ask for approval if it changes the approved methodology.

------------------------------------------------------------------------

# 12. MODEL MANAGEMENT RULES

Models must be loaded through dedicated modules.

Do not repeatedly initialize heavy models inside request functions.

Bad:

``` python
def analyze(text):
    model = SentenceTransformer(...)
```

Preferred:

``` python
model = load_sbert_model()

def analyze(text):
    embedding = model.encode(text)
```

Use lazy loading or application-level caching when appropriate.

------------------------------------------------------------------------

# 13. DEVICE MANAGEMENT

Support:

``` text
CPU
GPU / CUDA when available
```

Use configuration or automatic detection.

Example concept:

``` python
device = "cuda" if torch.cuda.is_available() else "cpu"
```

Do not assume GPU availability.

The application must remain usable on CPU for the academic prototype.

------------------------------------------------------------------------

# 14. FILE HANDLING RULES

Never trust uploaded filenames.

Validate:

-   Extension
-   MIME/type where applicable
-   File size
-   Readability
-   Image dimensions

Use safe temporary directories.

Never execute uploaded files.

Do not store arbitrary user-provided paths.

------------------------------------------------------------------------

# 15. DATASET RULES

The dataset must be treated as a research asset.

Maintain clear separation:

``` text
data/
├── raw/
├── processed/
├── metadata/
├── repository/
└── evaluation/
```

Never overwrite raw data during preprocessing.

Preferred:

``` text
raw image
   ↓
processed image
```

rather than modifying the original file.

------------------------------------------------------------------------

# 16. GROUND-TRUTH RULE

For evaluation, preserve ground truth separately from model output.

Example:

``` text
ground_truth_text
        ≠
ocr_text
```

Never replace ground-truth labels with predicted labels.

Never manually adjust labels to improve model metrics.

------------------------------------------------------------------------

# 17. EXPERIMENT TRACKING

Every meaningful experiment should record:

``` text
Experiment ID
Date
Dataset version
Model
Model version
OCR engine
Preprocessing configuration
Top-k
Similarity method
Scoring weights
Metrics
Processing time
Notes
```

Example:

``` yaml
experiment_id: EXP-001
ocr_engine: trocr
embedding_model: <model-name>
top_k: 5
lexical_weight: 0.0
semantic_weight: 0.0
contextual_weight: 0.0
ocr_weight: 0.0
```

Do not overwrite previous experimental results.

------------------------------------------------------------------------

# 18. REPRODUCIBILITY RULES

Where practical:

-   Set random seeds.
-   Record model versions.
-   Record dataset versions.
-   Record configuration.
-   Record package versions.
-   Record hardware/device.
-   Record experiment IDs.

A result should be reproducible from documented configuration.

------------------------------------------------------------------------

# 19. EVALUATION RULES

The project should evaluate:

### OCR

-   OCR Accuracy
-   OCR Confidence
-   Processing Time

### Plagiarism / Similarity

-   Precision
-   Recall
-   F1-score
-   Accuracy
-   Cosine Similarity
-   Final Plagiarism Score
-   Processing Time

Do not report metrics that have not actually been calculated.

Do not fabricate:

``` text
92% accuracy
95% F1
98% plagiarism detection
```

unless those values are produced by a documented experiment.

------------------------------------------------------------------------

# 20. BASELINE RULE

Before claiming that the hybrid approach improves performance, establish
comparable baselines.

Possible comparisons:

``` text
TF-IDF only
SBERT only
Cross-Encoder only
Hybrid approach
```

Use the same evaluation data and clearly document experimental
conditions.

Do not claim a winner without measurements.

------------------------------------------------------------------------

# 21. PLAGIARISM SCORE RULES

The final plagiarism score is an analytical model output.

It must not be presented as an unquestionable fact.

The UI should preferably expose supporting information:

``` text
Final Score
OCR Confidence
Lexical Similarity
Semantic Similarity
Contextual Similarity
Top Similar Documents
```

Avoid statements such as:

``` text
"This student definitely plagiarized."
```

Prefer:

``` text
"High similarity detected with the following documents."
```

The system is intended to support analysis, not replace human academic
judgment.

------------------------------------------------------------------------

# 22. THRESHOLD RULES

Do not hard-code labels such as:

``` text
0–20 = Safe
21–50 = Moderate
51–100 = Plagiarism
```

unless these thresholds are explicitly defined and validated by the
project team.

Thresholds must be:

-   Configurable
-   Documented
-   Experimentally evaluated

------------------------------------------------------------------------

# 23. OCR CONFIDENCE RULES

OCR confidence measures recognition confidence, not plagiarism.

Never interpret:

``` text
OCR confidence = plagiarism confidence
```

They are different signals.

Correct conceptual separation:

``` text
OCR Confidence
    ↓
Quality / reliability of extracted text

Similarity Scores
    ↓
Similarity between documents
```

They may contribute to a final analytical score only through the
approved scoring methodology.

------------------------------------------------------------------------

# 24. RETRIEVAL RULES

Semantic retrieval should produce ranked candidate documents.

Example:

``` json
[
  {
    "document_id": "DOC-001",
    "similarity": 0.91
  },
  {
    "document_id": "DOC-017",
    "similarity": 0.87
  }
]
```

Do not claim that top-k retrieval itself proves plagiarism.

Retrieval identifies candidates for deeper analysis.

------------------------------------------------------------------------

# 25. HYBRID MODEL RULES

Keep individual scores available.

Do not only return:

``` text
0.82
```

Return:

``` json
{
  "lexical_similarity": 0.00,
  "semantic_similarity": 0.00,
  "contextual_similarity": 0.00,
  "hybrid_similarity": 0.00
}
```

This makes the system easier to debug and evaluate.

------------------------------------------------------------------------

# 26. API RULES

If an API layer is implemented, keep endpoints focused.

Example:

``` text
POST /api/upload
POST /api/analyze
GET  /api/results/{id}
GET  /api/documents/{id}
GET  /api/health
```

Do not place model implementation directly inside route handlers.

Preferred:

``` text
API Route
   ↓
Service
   ↓
Pipeline Module
   ↓
Model
```

------------------------------------------------------------------------

# 27. SERVICE LAYER RULE

Use services to coordinate business logic.

Example:

``` text
analysis_service.py
```

may coordinate:

``` text
preprocessing
→ OCR
→ text preprocessing
→ retrieval
→ similarity
→ scoring
```

Individual modules should remain independently testable.

------------------------------------------------------------------------

# 28. DATABASE / STORAGE RULES

If persistent storage is implemented, separate:

``` text
Documents
Metadata
Embeddings
Analysis Results
Experiments
```

Do not mix binary document data and analytical results unnecessarily.

The exact database technology may be selected later according to project
implementation needs.

------------------------------------------------------------------------

# 29. ERROR HANDLING

Errors must be explicit.

Use custom exceptions where useful:

``` python
class OCRProcessingError(Exception):
    pass

class DocumentValidationError(Exception):
    pass

class RetrievalError(Exception):
    pass
```

Never silently return:

``` python
None
```

when a critical model step failed.

------------------------------------------------------------------------

# 30. LOGGING

Use structured logging for important operations.

Log:

-   Processing start
-   Document ID
-   OCR engine
-   OCR completion
-   Retrieval completion
-   Candidate count
-   Similarity completion
-   Final scoring completion
-   Processing duration
-   Errors

Do not log sensitive document content unnecessarily.

------------------------------------------------------------------------

# 31. TESTING RULES

Every major module should have tests.

Minimum testing structure:

``` text
tests/
├── test_preprocessing.py
├── test_ocr.py
├── test_text_processing.py
├── test_embeddings.py
├── test_retrieval.py
├── test_tfidf.py
├── test_cross_encoder.py
├── test_scoring.py
└── test_pipeline.py
```

------------------------------------------------------------------------

# 32. UNIT TEST RULES

Test:

### Preprocessing

-   Valid image
-   Empty input
-   Invalid image
-   Different dimensions

### OCR

-   Valid document
-   OCR failure
-   Empty OCR result
-   Confidence handling

### Similarity

-   Identical text
-   Different text
-   Empty text
-   Short text

### Scoring

-   Valid scores
-   Boundary values
-   Missing component
-   Configuration validation

------------------------------------------------------------------------

# 33. INTEGRATION TEST

The minimum end-to-end test must verify:

``` text
Upload
 ↓
Preprocess
 ↓
OCR
 ↓
Text
 ↓
Embedding
 ↓
Retrieval
 ↓
Hybrid Similarity
 ↓
Final Score
 ↓
Result
```

The complete pipeline should work before declaring the MVP complete.

------------------------------------------------------------------------

# 34. CODE REVIEW RULES FOR AI

Before returning code, the AI must check:

-   Does this code fit the architecture?
-   Is the module responsible for only one concern?
-   Is configuration hard-coded?
-   Is error handling present?
-   Is the code testable?
-   Are dependencies justified?
-   Does the implementation preserve raw data?
-   Does the implementation generate unsupported claims?
-   Are model outputs clearly distinguished from ground truth?
-   Does this change affect another module?

If yes, update or propose the required integration changes.

------------------------------------------------------------------------

# 35. AI CHANGE MANAGEMENT RULE

When modifying existing code:

1.  Read the relevant module first.
2.  Understand current behavior.
3.  Identify dependencies.
4.  Make the smallest safe change.
5.  Run relevant tests.
6.  Check integration.
7.  Explain the change.

Do not rewrite an entire project when only one module needs
modification.

------------------------------------------------------------------------

# 36. NO BLIND REWRITE RULE

Never replace working code simply because another implementation is
stylistically preferred.

Only rewrite when:

-   It fixes a real bug.
-   It is required by architecture.
-   It improves maintainability significantly.
-   It resolves a measured performance problem.
-   The user explicitly requests refactoring.

------------------------------------------------------------------------

# 37. NO SCOPE CREEP RULE

Do not add features such as:

-   Multilingual OCR
-   Cloud deployment
-   Authentication
-   Mobile application
-   Advanced dashboards
-   Vector database
-   PDF reporting
-   Real-time collaboration

unless they are requested or explicitly moved into the active
development scope.

These may remain future enhancements.

------------------------------------------------------------------------

# 38. DOCUMENTATION RULE

Every major module should have documentation covering:

``` text
Purpose
Input
Output
Dependencies
Configuration
Failure Cases
Example
Testing
```

Example:

``` markdown
## Adaptive OCR

### Input
Preprocessed document image.

### Output
Extracted text + OCR confidence.

### Engines
Tesseract / EasyOCR / TrOCR.

### Failure Cases
- Invalid image
- Empty OCR result
- Model unavailable
```

------------------------------------------------------------------------

# 39. README RULE

The project README should eventually contain:

1.  Project overview
2.  Problem statement
3.  Architecture
4.  Features
5.  Technology stack
6.  Installation
7.  Configuration
8.  Dataset setup
9.  Running the application
10. Running tests
11. Evaluation
12. Results
13. Limitations
14. Future scope

Never place fake benchmark results in README.

------------------------------------------------------------------------

# 40. GIT RULES

Use meaningful commits.

Good:

``` text
feat: add image preprocessing pipeline
feat: integrate TrOCR
feat: add SBERT retrieval
feat: implement TF-IDF similarity
feat: add Cross-Encoder scoring
test: add OCR pipeline tests
fix: handle empty OCR output
```

Avoid:

``` text
update
changes
final
final2
new
working
```

------------------------------------------------------------------------

# 41. BRANCHING

Recommended:

``` text
main
develop
feature/image-preprocessing
feature/ocr
feature/sbert-retrieval
feature/plagiarism
feature/evaluation
feature/frontend
```

Do not directly merge untested experimental code into the stable branch.

------------------------------------------------------------------------

# 42. DATA PRIVACY RULE

Documents may contain academic or personal information.

Therefore:

-   Do not expose uploaded content in logs.
-   Do not commit datasets containing sensitive content to Git.
-   Do not commit credentials.
-   Do not commit API keys.
-   Use `.env` for secrets.
-   Add sensitive paths to `.gitignore`.

------------------------------------------------------------------------

# 43. SECRET MANAGEMENT

Never write:

``` python
API_KEY = "actual-secret"
```

Use:

``` text
.env
```

and environment variables.

The `.env` file must not be committed.

------------------------------------------------------------------------

# 44. PERFORMANCE RULES

Measure before optimizing.

Track:

``` text
Preprocessing Time
OCR Time
Embedding Time
Retrieval Time
TF-IDF Time
Cross-Encoder Time
Total Time
```

Do not optimize based only on assumptions.

------------------------------------------------------------------------

# 45. MEMORY RULES

OCR and transformer models can consume substantial memory.

Avoid:

-   Loading the same model repeatedly.
-   Keeping unnecessary images in memory.
-   Encoding the entire repository on every request.

Prefer:

``` text
Precompute repository embeddings
        ↓
Store embeddings
        ↓
Query them during analysis
```

------------------------------------------------------------------------

# 46. REPOSITORY EMBEDDING RULE

Repository embeddings should be generated as a separate indexing process
when practical.

Conceptually:

``` text
Documents
    ↓
Text Preprocessing
    ↓
SBERT
    ↓
Embeddings
    ↓
Repository Index
```

Then:

``` text
New Document
    ↓
SBERT
    ↓
Query Embedding
    ↓
Repository Index
    ↓
Top-K
```

Do not unnecessarily recompute all repository embeddings for every
uploaded document.

------------------------------------------------------------------------

# 47. CACHE RULE

Cache only deterministic and reusable expensive results where
appropriate.

Potential cache targets:

-   Repository embeddings
-   Loaded models
-   Preprocessed repository text

Do not cache user-specific results without a clear invalidation
strategy.

------------------------------------------------------------------------

# 48. MODEL VERSIONING

Record the model identifier/version used for:

-   OCR
-   SBERT
-   Cross-Encoder

Do not silently change models between experiments.

If the model changes:

``` text
Create a new experiment configuration.
```

------------------------------------------------------------------------

# 49. RESEARCH INTEGRITY RULE

The AI must never:

-   Fabricate experimental results.
-   Fabricate dataset statistics.
-   Fabricate citations.
-   Claim a model is better without evaluation.
-   Change ground truth.
-   Manipulate evaluation data.
-   Hide failed experiments.
-   Present assumptions as measured facts.

If information is unknown:

``` text
State that it is unknown.
```

------------------------------------------------------------------------

# 50. EXPLANATION RULE

When making a significant implementation decision, explain:

``` text
Decision
Why
Impact
Alternative
```

Example:

``` text
Decision:
Use SBERT embeddings for candidate retrieval.

Why:
The approved architecture uses semantic retrieval to reduce the
candidate search space before detailed hybrid analysis.

Impact:
Only top-k candidates proceed to expensive similarity analysis.

Alternative:
Full pairwise comparison, but it is less efficient for larger repositories.
```

------------------------------------------------------------------------

# 51. WHEN TO ASK FOR CLARIFICATION

Ask before coding if any of these are unclear:

-   Final scoring formula
-   Final hybrid weights
-   Dataset format
-   Ground-truth definition
-   OCR selection criteria
-   Model replacement
-   Database choice when architecture is affected
-   API contract
-   UI behavior that changes research methodology

Do not ask unnecessary questions when a documented project decision
already exists.

------------------------------------------------------------------------

# 52. WHEN NOT TO ASK

Do not ask for permission for routine implementation choices that do not
change architecture.

Examples:

-   Variable names
-   Function names
-   File organization within an approved module
-   Unit-test structure
-   Logging format
-   Basic exception handling
-   Minor UI spacing

Use reasonable engineering judgment.

------------------------------------------------------------------------

# 53. AI RESPONSE FORMAT FOR DEVELOPMENT TASKS

When implementing a task, prefer:

``` text
## Task
What is being implemented.

## Files Changed
- file1.py
- file2.py

## Implementation
Short explanation.

## Architecture Impact
None / describe impact.

## Testing
Tests executed and results.

## Notes
Known limitations or next steps.
```

Do not provide long explanations when the user only asks for a small
code change.

------------------------------------------------------------------------

# 54. FEATURE IMPLEMENTATION CHECKLIST

Before marking a feature complete:

``` text
[ ] Requirement understood
[ ] Architecture checked
[ ] Module identified
[ ] Implementation completed
[ ] Configuration added
[ ] Error handling added
[ ] Tests added
[ ] Tests passed
[ ] Documentation updated
[ ] No secrets committed
[ ] No raw dataset modified
[ ] No unsupported claims
```

------------------------------------------------------------------------

# 55. MODULE COMPLETION CHECKLIST

A module is complete when:

``` text
[ ] Clear input
[ ] Clear output
[ ] Independent implementation
[ ] Unit tests
[ ] Error handling
[ ] Configuration
[ ] Documentation
[ ] Integration tested
```

------------------------------------------------------------------------

# 56. MVP COMPLETION CHECKLIST

The MVP is complete when:

``` text
[ ] Document upload works
[ ] Image preprocessing works
[ ] OCR works
[ ] OCR confidence is captured
[ ] Text preprocessing works
[ ] SBERT embeddings work
[ ] Top-k retrieval works
[ ] TF-IDF similarity works
[ ] SBERT similarity works
[ ] Cross-Encoder works
[ ] Hybrid similarity works
[ ] Final score works
[ ] Results are displayed
[ ] Evaluation pipeline works
[ ] End-to-end test passes
```

------------------------------------------------------------------------

# 57. FINAL DEVELOPMENT PIPELINE

The AI should think in this sequence for every major task:

``` text
UNDERSTAND
    ↓
CHECK REQUIREMENTS
    ↓
CHECK ARCHITECTURE
    ↓
IDENTIFY MODULE
    ↓
IMPLEMENT MINIMUM CHANGE
    ↓
TEST
    ↓
INTEGRATE
    ↓
DOCUMENT
    ↓
VERIFY
```

Never:

``` text
Guess
 ↓
Rewrite everything
 ↓
Add dependencies
 ↓
Claim it works
```

------------------------------------------------------------------------

# 58. GOLDEN RULES

## Rule 1 --- Architecture First

Do not violate the approved architecture for convenience.

## Rule 2 --- Evidence Over Assumption

Do not invent project facts, results, datasets, or model performance.

## Rule 3 --- Modular by Default

Every major pipeline stage should be independently testable.

## Rule 4 --- Configuration Over Hard-Coding

Models, thresholds, paths, top-k, and weights belong in configuration.

## Rule 5 --- Preserve Data

Never overwrite raw documents or ground truth.

## Rule 6 --- Reproducibility Matters

Record model versions, configurations, datasets, and experiment
settings.

## Rule 7 --- Test Before Claiming

Never say "working" without appropriate testing.

## Rule 8 --- Research Integrity

Never fabricate or manipulate results.

## Rule 9 --- Human Interpretation

A plagiarism score is an analytical signal, not an automatic academic
misconduct verdict.

## Rule 10 --- Small Safe Changes

Prefer incremental, reviewable changes over blind rewrites.

------------------------------------------------------------------------

# 59. FINAL AI INSTRUCTION

When asked to build or modify this project, follow this hierarchy:

``` text
                    PROJECT PRD
                         │
                         ↓
                  ARCHITECTURE
                         │
                         ↓
              DEVELOPMENT RULES
                         │
                         ↓
                  CURRENT TASK
                         │
                         ↓
              IMPLEMENT + TEST
                         │
                         ↓
                VERIFY + DOCUMENT
```

The AI must preserve the project's core methodology:

``` text
Image Preprocessing
        ↓
Adaptive OCR
        ↓
Text + OCR Confidence
        ↓
Text Preprocessing
        ↓
SBERT Retrieval
        ↓
Top-K Candidates
        ↓
TF-IDF + SBERT + Cross-Encoder
        ↓
Hybrid Similarity
        ↓
Weighted Final Scoring
        ↓
Evaluation + Results
```

**Do not silently replace, skip, or fundamentally alter a core stage.**

If a change is necessary, clearly identify:

``` text
WHAT changed
WHY it changed
WHICH architecture component is affected
WHAT alternatives were considered
HOW the change will be evaluated
```

This document is the default engineering contract for AI-assisted
development of the project.
