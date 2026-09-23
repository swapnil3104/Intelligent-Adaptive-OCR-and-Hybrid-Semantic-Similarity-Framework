# DESIGN.md

# UI/UX Design Specification --- Intelligent Adaptive OCR and Hybrid Semantic Similarity Framework

> **Purpose:** This document defines the visual design system, UX
> structure, screen architecture, interaction patterns, accessibility
> requirements, and UI implementation rules for the project.
>
> **Design principle:** The interface must make a technically complex
> AI/OCR pipeline understandable to students, faculty, and evaluators
> without overwhelming them with implementation details.

------------------------------------------------------------------------

# 1. Design Goals

The application should communicate four things clearly:

1.  **What document is being analyzed**
2.  **What the OCR system extracted**
3.  **Which documents are similar**
4.  **Why the final similarity/plagiarism score was produced**

The UI should feel:

-   Professional
-   Academic
-   Modern
-   Clean
-   Trustworthy
-   Data-focused
-   Easy to demonstrate during a project presentation

Avoid unnecessary decorative elements that distract from the analysis
workflow.

------------------------------------------------------------------------

# 2. Primary User Flow

The primary experience is:

``` text
Home
  ↓
Upload Document
  ↓
Document Preview
  ↓
Processing
  ↓
OCR Result
  ↓
Similarity Analysis
  ↓
Final Results
  ↓
Detailed Comparison
```

The user should always know:

``` text
Where am I?
What is happening?
What should I do next?
```

------------------------------------------------------------------------

# 3. Information Architecture

Recommended application structure:

``` text
Application
│
├── Dashboard / Home
│
├── Analyze Document
│   ├── Upload
│   ├── Preview
│   └── Processing
│
├── Analysis Result
│   ├── Overview
│   ├── OCR
│   ├── Similar Documents
│   ├── Similarity Breakdown
│   └── Evidence
│
├── Documents
│   └── Repository
│
├── Evaluation
│   ├── OCR Metrics
│   ├── Retrieval Metrics
│   └── Plagiarism Metrics
│
└── Settings
```

For the MVP, the minimum navigation can be:

``` text
Dashboard
Analyze
Results
```

------------------------------------------------------------------------

# 4. Visual Design Direction

## Overall Style

Use a modern academic AI dashboard style.

Characteristics:

``` text
Clean layouts
Generous spacing
Rounded cards
Subtle borders
Minimal shadows
Clear typography
Strong information hierarchy
```

Avoid:

``` text
Excessive gradients
Heavy glassmorphism
Large decorative illustrations
Overly animated backgrounds
Cluttered dashboards
Too many colors
```

------------------------------------------------------------------------

# 5. Design Language

The interface should communicate:

``` text
AI + Computer Vision + NLP + Academic Research
```

The visual language should therefore combine:

-   Technical precision
-   Research credibility
-   Friendly usability

------------------------------------------------------------------------

# 6. Color System

Use a restrained color palette.

## Primary

A deep blue / indigo family can represent:

``` text
AI
Trust
Technology
Research
```

## Secondary

Use a neutral slate/gray palette for:

``` text
Backgrounds
Borders
Secondary text
Tables
Metadata
```

## Status Colors

Use semantic colors only when necessary:

  State     Suggested Meaning
  --------- ----------------------------
  Success   Completed / valid
  Warning   Needs attention
  Error     Failed
  Info      Processing / informational

Do not use status colors merely for decoration.

------------------------------------------------------------------------

# 7. Color Usage Rule

The final similarity score must not rely on color alone.

For example:

``` text
82%
High Similarity
```

is preferable to showing only a red progress bar.

Always provide:

``` text
Number
+
Label
+
Context
```

This improves accessibility and comprehension.

------------------------------------------------------------------------

# 8. Typography

Use a clean modern sans-serif font.

Recommended hierarchy:

``` text
H1 → 36–48px
H2 → 28–36px
H3 → 20–24px
Body → 14–16px
Small → 12–14px
```

Use readable line height.

Recommended:

``` text
Body line-height ≈ 1.5–1.7
```

Do not use extremely thin font weights for important information.

------------------------------------------------------------------------

# 9. Spacing System

Use a consistent spacing scale.

Recommended base unit:

``` text
4px
```

Example:

``` text
4
8
12
16
20
24
32
40
48
64
```

Avoid arbitrary spacing values throughout the UI.

------------------------------------------------------------------------

# 10. Layout

Use a responsive container.

Desktop:

``` text
┌─────────────────────────────────────────────────────┐
│ Navigation                                           │
├─────────────────────────────────────────────────────┤
│                                                     │
│                Main Content Area                    │
│                                                     │
└─────────────────────────────────────────────────────┘
```

Recommended content width:

``` text
1200px – 1400px
```

depending on screen size.

------------------------------------------------------------------------

# 11. Navigation Design

Recommended desktop navigation:

``` text
┌──────────────────────────────────────────────────────┐
│ Logo / Project Name     Dashboard  Analyze  Results │
└──────────────────────────────────────────────────────┘
```

Mobile:

``` text
┌────────────────────────────┐
│ Logo                  ☰    │
└────────────────────────────┘
```

Navigation should remain visually simple.

------------------------------------------------------------------------

# 12. Branding

Suggested project name:

**Intelligent Adaptive OCR**

Optional short descriptor:

**Hybrid Semantic Similarity Framework**

Example:

``` text
┌─────────────────────────────┐
│ IA-OCR                      │
│ Intelligent Adaptive OCR    │
└─────────────────────────────┘
```

A simple OCR/document + AI-inspired icon can be used.

Do not make the logo visually complicated.

------------------------------------------------------------------------

# 13. Dashboard Design

The dashboard should immediately communicate system capabilities.

## Hero Area

``` text
------------------------------------------------------
Intelligent Adaptive OCR
Hybrid Semantic Similarity Framework

Analyze handwritten, scanned, and printed documents
using adaptive OCR and multi-level similarity analysis.

[ Analyze Document ]
------------------------------------------------------
```

## Capability Cards

``` text
┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│ Adaptive OCR│ │ SBERT       │ │ Hybrid      │
│             │ │ Retrieval   │ │ Similarity  │
└─────────────┘ └─────────────┘ └─────────────┘
```

------------------------------------------------------------------------

# 14. Analyze Page

The Analyze page is the most important input screen.

## Layout

``` text
┌─────────────────────────────────────────────────────┐
│ Analyze Document                                    │
├─────────────────────────────────────────────────────┤
│                                                     │
│              ┌───────────────────┐                  │
│              │                   │                  │
│              │   Upload File     │                  │
│              │                   │                  │
│              │  Drag & Drop      │                  │
│              │       or          │                  │
│              │   Choose File     │                  │
│              │                   │                  │
│              └───────────────────┘                  │
│                                                     │
│ Supported: JPG / PNG / PDF*                         │
│                                                     │
│                 [ Analyze ]                         │
└─────────────────────────────────────────────────────┘
```

Only display file types that the backend actually supports.

------------------------------------------------------------------------

# 15. Upload Component

The upload component should support:

### Default

``` text
Drag and drop your document here

or

Browse Files
```

### Selected

``` text
✓ document.jpg

1.8 MB

[Replace] [Remove]
```

### Invalid

``` text
⚠ Unsupported file type

Please upload a supported document.
```

### Processing

``` text
Uploading...
██████████░░░░ 65%
```

------------------------------------------------------------------------

# 16. Document Preview

After upload, show a preview.

``` text
┌─────────────────────┐
│                     │
│   Document Preview  │
│                     │
│      IMAGE          │
│                     │
└─────────────────────┘

Filename: assignment.jpg
Type: Handwritten
Size: 1.8 MB
```

If the document type is not actually detected, label it:

``` text
Type: Not classified
```

Do not invent document classifications.

------------------------------------------------------------------------

# 17. Processing Screen

The processing screen should expose pipeline progress.

``` text
Analyzing Document

✓ Image preprocessing
✓ OCR extraction
● Text processing
○ Semantic retrieval
○ Similarity analysis
○ Final scoring
```

This is better than displaying only:

``` text
Loading...
```

------------------------------------------------------------------------

# 18. Processing Step Design

Each step should have a state:

``` text
○ Pending
● Processing
✓ Completed
⚠ Warning
✕ Failed
```

Example:

``` text
✓ Image preprocessing        0.8s
✓ OCR extraction             4.2s
✓ Text preprocessing         0.1s
● Semantic retrieval         ...
○ Hybrid analysis
○ Final scoring
```

Only show timing information if the backend actually measures it.

------------------------------------------------------------------------

# 19. OCR Result Screen

The OCR section should show both the extracted text and OCR metadata.

``` text
┌─────────────────────────────────────────────────────┐
│ OCR Analysis                                        │
├─────────────────────────────────────────────────────┤
│                                                     │
│ OCR Engine          TrOCR                           │
│ Confidence          91%                             │
│ Processing Time     4.2s                            │
│                                                     │
├─────────────────────────────────────────────────────┤
│ Extracted Text                                      │
│                                                     │
│ Lorem ipsum dolor sit amet...                      │
│                                                     │
└─────────────────────────────────────────────────────┘
```

Do not present OCR confidence as plagiarism confidence.

------------------------------------------------------------------------

# 20. OCR Confidence Visualization

Recommended:

``` text
OCR Confidence

91%
██████████████████░░
High
```

Also provide the numeric value.

If confidence semantics differ between OCR engines, label the metric
appropriately.

------------------------------------------------------------------------

# 21. Similar Documents Section

The system should display the retrieved top-k candidates.

``` text
Similar Documents

┌─────────────────────────────────────────────────────┐
│ Document ID     Similarity      Analysis             │
├─────────────────────────────────────────────────────┤
│ DOC-001         91%             View                │
│ DOC-017         87%             View                │
│ DOC-042         81%             View                │
└─────────────────────────────────────────────────────┘
```

Do not label retrieved documents as plagiarized solely because they were
retrieved.

Use:

``` text
Similar Document
```

until the full scoring process supports a stronger interpretation.

------------------------------------------------------------------------

# 22. Result Overview

The top of the result page should provide an immediate summary.

``` text
Analysis Complete

┌──────────────────┐
│  Final Score     │
│                  │
│      82%         │
│  High Similarity │
└──────────────────┘

OCR Confidence: 91%
Candidates: 5
Processing Time: 8.7s
```

All displayed values must come from actual backend results.

------------------------------------------------------------------------

# 23. Score Breakdown

The final score should be explainable.

``` text
Similarity Breakdown

Lexical Similarity       76%
Semantic Similarity      88%
Contextual Similarity    84%
OCR Confidence           91%

────────────────────────────

Final Score              82%
```

The exact final formula must match the backend configuration.

Do not display weights that are not actually used.

------------------------------------------------------------------------

# 24. Score Visualization

Recommended visualization:

``` text
Final Score
     82%
      │
      ▼
┌───────────────────────┐
│     Similarity        │
│      82 / 100         │
└───────────────────────┘
```

A circular progress indicator may be used.

However:

-   Keep it simple.
-   Show the numeric value.
-   Provide a text label.
-   Do not rely only on color.

------------------------------------------------------------------------

# 25. Detailed Comparison View

The detailed comparison should allow the user to inspect why two
documents were considered similar.

``` text
┌─────────────────────────────────────────────────────┐
│ Document A                     Document B            │
├─────────────────────────────────────────────────────┤
│ Text paragraph...              Text paragraph...     │
│                                                     │
│ Similar phrases / concepts should be highlighted   │
└─────────────────────────────────────────────────────┘
```

Possible tabs:

``` text
Lexical
Semantic
Contextual
```

------------------------------------------------------------------------

# 26. Similarity Method Tabs

## Lexical

Explain:

``` text
TF-IDF + Cosine Similarity
```

## Semantic

Explain:

``` text
SBERT Embedding Similarity
```

## Contextual

Explain:

``` text
Cross-Encoder Pairwise Analysis
```

Keep explanations short in the main UI.

Provide detailed explanations in an optional information panel.

------------------------------------------------------------------------

# 27. Evidence Panel

Every high similarity result should have supporting evidence where
available.

Example:

``` text
Evidence

Matched Document: DOC-017

Lexical similarity: 76%
Semantic similarity: 88%
Contextual similarity: 84%

[View Document]
[View Comparison]
```

Avoid making unsupported claims about intent.

------------------------------------------------------------------------

# 28. Result Status

Use descriptive labels rather than definitive accusations.

Possible configurable labels:

``` text
Low Similarity
Moderate Similarity
High Similarity
```

Thresholds must come from validated project configuration.

Do not hard-code arbitrary thresholds in the frontend.

------------------------------------------------------------------------

# 29. Evaluation Dashboard

The Evaluation page is intended for developers, researchers, and project
evaluators.

Suggested sections:

``` text
Evaluation Overview

┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│ OCR Metric  │ │ Retrieval   │ │ F1 Score    │
│             │ │ Metric      │ │             │
└─────────────┘ └─────────────┘ └─────────────┘
```

------------------------------------------------------------------------

# 30. Evaluation Charts

Potential charts:

### OCR

``` text
OCR Performance by Engine
```

### Similarity

``` text
TF-IDF vs SBERT vs Cross-Encoder vs Hybrid
```

### Performance

``` text
Processing Time by Pipeline Stage
```

Only show charts for metrics actually measured.

------------------------------------------------------------------------

# 31. Repository Page

The document repository can display:

``` text
Documents

Search documents...

┌─────────────────────────────────────────────────────┐
│ ID       Type          Status        Embedding      │
├─────────────────────────────────────────────────────┤
│ DOC-001  Handwritten   Indexed       ✓              │
│ DOC-002  Printed       Indexed       ✓              │
│ DOC-003  Scanned       Pending       —              │
└─────────────────────────────────────────────────────┘
```

Do not expose document contents to unauthorized users.

------------------------------------------------------------------------

# 32. Empty States

Every major screen needs a useful empty state.

Example:

``` text
No analyses yet

Upload a document to start your first similarity analysis.

[ Analyze Document ]
```

Avoid empty screens.

------------------------------------------------------------------------

# 33. Error States

Errors should explain what happened and what the user can do.

Bad:

``` text
Error 500
```

Better:

``` text
Unable to process this document.

The uploaded image could not be read.

[ Try Another File ]
```

Do not expose internal stack traces to normal users.

------------------------------------------------------------------------

# 34. Warning States

Example:

``` text
⚠ Low OCR Confidence

The extracted text may contain recognition errors.
Review the OCR output before interpreting similarity results.
```

This is especially important because OCR quality directly affects
downstream text analysis.

------------------------------------------------------------------------

# 35. Loading States

Use skeletons or step-based progress for longer operations.

Example:

``` text
Preparing document...
Extracting text...
Finding similar documents...
Running hybrid analysis...
Preparing results...
```

Avoid fake progress percentages unless the backend provides meaningful
progress.

------------------------------------------------------------------------

# 36. Responsive Design

The application must work on:

``` text
Desktop
Laptop
Tablet
Mobile
```

Priority:

``` text
Desktop → Laptop → Tablet → Mobile
```

because the application is primarily an academic/project dashboard.

------------------------------------------------------------------------

# 37. Mobile Layout

Desktop:

``` text
┌────────────┬─────────────────────────────┐
│ Sidebar    │ Main Content                │
└────────────┴─────────────────────────────┘
```

Mobile:

``` text
┌────────────────────────────┐
│ Header                     │
├────────────────────────────┤
│ Content                    │
│                            │
│ Cards stack vertically     │
│ Tables become scrollable   │
└────────────────────────────┘
```

------------------------------------------------------------------------

# 38. Tables

Tables should:

-   Use clear headers.
-   Align numbers consistently.
-   Support horizontal scrolling on mobile.
-   Avoid unnecessary columns.
-   Highlight important values.

For mobile, use:

``` text
Card layout
```

when the table becomes too wide.

------------------------------------------------------------------------

# 39. Cards

Use cards for:

-   Metrics
-   OCR information
-   Similar documents
-   Pipeline status
-   Evaluation results

Card anatomy:

``` text
┌─────────────────────────┐
│ Label                   │
│                         │
│ Large Value             │
│ Supporting information  │
└─────────────────────────┘
```

Do not nest too many cards.

------------------------------------------------------------------------

# 40. Buttons

Primary actions:

``` text
Analyze Document
Run Analysis
View Results
```

Secondary:

``` text
Replace
Cancel
Back
View Details
```

Destructive:

``` text
Delete
Remove
```

Destructive actions should require confirmation when appropriate.

------------------------------------------------------------------------

# 41. Button Hierarchy

Only one primary action should dominate a section.

Example:

``` text
[ Analyze Document ]   Replace
```

not:

``` text
[Analyze] [Run] [Process] [Submit] [Start]
```

when all actions perform essentially the same operation.

------------------------------------------------------------------------

# 42. Tooltips

Use tooltips for technical terms:

``` text
SBERT
TF-IDF
Cross-Encoder
Cosine Similarity
OCR Confidence
```

Example:

``` text
Semantic Similarity ⓘ
```

Tooltip:

``` text
Measures similarity between document meanings
using sentence embeddings.
```

------------------------------------------------------------------------

# 43. Technical Information Panel

Advanced users can expand:

``` text
Technical Details
```

Show:

``` text
OCR Engine
OCR Model
Embedding Model
Cross-Encoder
Top-K
Similarity Configuration
Processing Time
Experiment ID
```

This keeps the main UI simple while preserving research transparency.

------------------------------------------------------------------------

# 44. Accessibility

The interface must support:

-   Keyboard navigation
-   Visible focus states
-   Semantic HTML
-   Accessible labels
-   Sufficient contrast
-   Screen-reader-friendly status messages
-   Non-color-only status communication

Do not communicate meaning using color alone.

------------------------------------------------------------------------

# 45. Form Accessibility

Upload controls must have clear labels.

Bad:

``` text
[Choose]
```

Better:

``` text
Upload document
[Choose File]
```

Errors should be associated with the relevant control.

------------------------------------------------------------------------

# 46. Animation

Use subtle animation only when it improves feedback.

Good:

``` text
Upload transition
Progress indicator
Card appearance
Loading skeleton
```

Avoid:

``` text
Constant moving backgrounds
Large animations
Unnecessary transitions
```

Respect reduced-motion preferences.

------------------------------------------------------------------------

# 47. Microcopy

Use concise, human-readable language.

Prefer:

``` text
Analyze your document
```

instead of:

``` text
Execute document inference pipeline
```

Prefer:

``` text
Finding similar documents...
```

instead of:

``` text
Executing SBERT vector retrieval subsystem
```

Technical details belong in the advanced section.

------------------------------------------------------------------------

# 48. Trust and Transparency

Because the application produces AI-assisted analytical results, the UI
should make the system's process visible.

Recommended:

``` text
How was this result calculated?

1. Image was processed
2. Text was extracted
3. Similar documents were retrieved
4. Lexical similarity was measured
5. Semantic similarity was measured
6. Contextual similarity was measured
7. Final score was calculated
```

This should be accessible from the results page.

------------------------------------------------------------------------

# 49. Result Disclaimer

The application should include concise contextual language such as:

> **Similarity results are analytical indicators and should be reviewed
> with the underlying document evidence.**

Do not present the system as making a definitive academic misconduct
determination.

------------------------------------------------------------------------

# 50. Frontend Component Architecture

Suggested component structure:

``` text
src/
│
├── components/
│   ├── layout/
│   │   ├── Header
│   │   ├── Sidebar
│   │   └── PageContainer
│   │
│   ├── upload/
│   │   ├── UploadZone
│   │   ├── FilePreview
│   │   └── UploadStatus
│   │
│   ├── processing/
│   │   ├── PipelineProgress
│   │   └── ProcessingStep
│   │
│   ├── results/
│   │   ├── ScoreCard
│   │   ├── ScoreBreakdown
│   │   ├── OCRResult
│   │   ├── SimilarDocuments
│   │   └── EvidencePanel
│   │
│   └── evaluation/
│       ├── MetricCard
│       ├── PerformanceChart
│       └── EvaluationTable
│
├── pages/
│   ├── Dashboard
│   ├── Analyze
│   ├── Results
│   ├── Repository
│   └── Evaluation
│
├── services/
│   └── api
│
├── hooks/
├── utils/
└── styles/
```

------------------------------------------------------------------------

# 51. Frontend State Model

The UI should represent analysis state explicitly.

``` text
idle
 ↓
uploading
 ↓
uploaded
 ↓
processing
 ↓
completed
```

Error:

``` text
processing
 ↓
failed
```

Result data should be separated from UI state.

Example concept:

``` javascript
{
  status: "completed",
  result: {
    ocrConfidence: 0.91,
    lexicalSimilarity: 0.76,
    semanticSimilarity: 0.88,
    contextualSimilarity: 0.84,
    finalScore: 0.82
  }
}
```

The actual API schema must be defined by the backend contract.

------------------------------------------------------------------------

# 52. Design System Tokens

Centralize design tokens.

Example:

``` text
tokens/
├── colors
├── typography
├── spacing
├── radius
├── shadows
└── breakpoints
```

Do not duplicate visual constants throughout components.

------------------------------------------------------------------------

# 53. Border Radius

Use a restrained radius system.

Example:

``` text
Small: 6px
Medium: 10px
Large: 14px
```

Use consistent values throughout the application.

------------------------------------------------------------------------

# 54. Shadows

Prefer subtle shadows.

Avoid:

``` text
Heavy card shadows
```

Recommended visual hierarchy:

``` text
Border first
Shadow second
```

Many cards can use borders without shadows.

------------------------------------------------------------------------

# 55. Iconography

Use one consistent icon library.

Icons should:

-   Have consistent stroke/weight.
-   Support accessibility labels where necessary.
-   Never replace essential text labels by themselves.

Example:

``` text
[↑ Upload]
[↻ Retry]
[✓ Complete]
[⚠ Warning]
```

------------------------------------------------------------------------

# 56. Dashboard Metric Cards

Recommended metrics:

``` text
Documents Analyzed
Average OCR Confidence
Average Similarity
Average Processing Time
```

Only display aggregate metrics when the backend has enough data to
calculate them.

------------------------------------------------------------------------

# 57. Design for Demonstration

The project will likely be demonstrated during an academic evaluation.

Therefore, the main demo flow should be extremely clear:

``` text
1. Upload document
2. Show document preview
3. Show processing pipeline
4. Show OCR output
5. Show similar documents
6. Show similarity breakdown
7. Show final result
```

Avoid requiring the evaluator to navigate through multiple unrelated
screens.

------------------------------------------------------------------------

# 58. Demo Mode

If a demo mode is implemented, it must use clearly labeled sample data.

Example:

``` text
Demo Dataset
```

Do not mix demo data with real user documents without clear labeling.

------------------------------------------------------------------------

# 59. Frontend Performance

Avoid:

-   Rendering very large extracted text unnecessarily.
-   Loading all repository documents at once.
-   Re-running expensive visualizations on every render.
-   Re-fetching results unnecessarily.

Use pagination, virtualization, or lazy loading where justified.

------------------------------------------------------------------------

# 60. API Loading UX

The frontend should never freeze while AI models process a document.

Use:

``` text
Upload → Processing state → Result
```

If processing can take a long time, use a job/status architecture:

``` text
POST /analyze
      ↓
job_id
      ↓
GET /analysis/{job_id}
      ↓
status
      ↓
completed
```

Only implement this complexity if required by the backend architecture.

------------------------------------------------------------------------

# 61. Design Rules for AI Coding Agents

When an AI agent creates or modifies frontend code, it must:

1.  Follow this design system.
2.  Reuse existing components.
3.  Avoid unnecessary new dependencies.
4.  Keep layouts responsive.
5.  Preserve accessibility.
6.  Avoid introducing random colors.
7.  Avoid inconsistent spacing.
8.  Keep technical details separate from primary UX.
9.  Never fabricate backend data.
10. Use loading, empty, error, and success states.

------------------------------------------------------------------------

# 62. Do Not Hard-Code Results

Never write:

``` javascript
const score = 82;
```

as a permanent UI result.

The frontend must consume actual backend output.

If mock data is required during development, label it clearly:

``` text
MOCK DATA
```

and isolate it from production logic.

------------------------------------------------------------------------

# 63. Do Not Hard-Code Thresholds

Avoid:

``` javascript
if (score > 80) {
  label = "High";
}
```

unless `80` is defined by the approved backend/configuration.

Prefer:

``` text
Backend/configuration → threshold → frontend label
```

------------------------------------------------------------------------

# 64. Frontend/Backend Contract

The frontend should not infer missing analytical values.

For example, if the backend returns:

``` json
{
  "semantic_similarity": 0.88
}
```

do not invent:

``` json
{
  "lexical_similarity": 0.80
}
```

Missing values should be represented explicitly.

------------------------------------------------------------------------

# 65. Design QA Checklist

Before a UI feature is complete:

``` text
[ ] Desktop layout works
[ ] Mobile layout works
[ ] Loading state exists
[ ] Empty state exists
[ ] Error state exists
[ ] Success state exists
[ ] Keyboard navigation works
[ ] Focus states are visible
[ ] Labels are clear
[ ] Color is not the only status indicator
[ ] No fake data in production
[ ] No hard-coded analytical results
[ ] Typography is consistent
[ ] Spacing is consistent
[ ] Buttons have clear hierarchy
[ ] Technical terminology has explanations
```

------------------------------------------------------------------------

# 66. Final Design Principle

The interface should make the following journey visually obvious:

``` text
┌──────────────┐
│   DOCUMENT   │
└──────┬───────┘
       ↓
┌──────────────┐
│  IMAGE       │
│ PREPROCESSING│
└──────┬───────┘
       ↓
┌──────────────┐
│     OCR      │
└──────┬───────┘
       ↓
┌──────────────┐
│     TEXT     │
└──────┬───────┘
       ↓
┌──────────────┐
│   SBERT      │
│  RETRIEVAL   │
└──────┬───────┘
       ↓
┌─────────────────────┐
│ HYBRID SIMILARITY   │
│ TF-IDF + SBERT + CE │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│ FINAL ANALYSIS      │
└─────────────────────┘
```

The UI should expose enough information for the user to understand
**what happened and why**, while keeping the primary workflow simple.

------------------------------------------------------------------------

# 67. Design Golden Rules

### Rule 1 --- Clarity Over Decoration

The interface is an AI research tool, not a visual showcase.

### Rule 2 --- Explain AI Results

Show supporting signals, not only the final number.

### Rule 3 --- Never Fabricate Data

Every displayed analytical value must come from actual data or clearly
labeled mock data.

### Rule 4 --- Keep Technical Complexity Progressive

Basic users see the result; advanced users can expand technical details.

### Rule 5 --- Accessibility Is Mandatory

Color, icons, and animation must not replace meaningful text.

### Rule 6 --- Consistency Matters

Use the same spacing, typography, buttons, cards, and status patterns
everywhere.

### Rule 7 --- Preserve Trust

Clearly distinguish:

``` text
OCR confidence
Similarity
Final analytical score
```

### Rule 8 --- Design Around the Pipeline

The UI should mirror the actual architecture:

``` text
Upload
→ OCR
→ Retrieval
→ Similarity
→ Result
```

### Rule 9 --- Responsive by Default

Every important workflow must remain usable on smaller screens.

### Rule 10 --- Human Review

Similarity results should support human review rather than being
presented as an unquestionable final judgment.
