# Week 3 Project: Content-Based AI Recommendation Engine

This directory contains my notebook implementation blueprint for Project 3 under the DecodeLabs AI Engineering Training Track. The intent of this system is to shift from passive data classification into active user predictive modeling, solving choice overload through structured logic matching.

##  The Architectural IPO Pipeline

This engine processes user query matrices using content-based filtering principles in an interactive notebook interface, running completely independent of external community datasets.

### 1. Information Ingestion (Input Layer)
* The notebook cell accepts an input density of exactly three user baseline skills or high-retention career goals to create an atomic vector profile.

### 2. Feature Extraction Framework (Process Layer)
* **TF-IDF Statistical Weighting:** Transforms raw string values into numerical vectors. The inverse document frequency dampens generic terms while magnifying specific technical competencies.
* **Cosine Similarity Scoring:** Evaluates matching orientation between the vector matrices based on dot products, remaining completely invariant to magnitude differences.

### 3. Truncated Top-N List (Output Layer)
* Sorts raw similarity returns in descending order and applies a hard filtering limit to surface only the Top 3 highest-ranking matches.
* **Cold Start Fallback Protection:** Integrated a programmatic trending bypass. If a new user enters zero correlating vector metrics, the system suppresses mathematical system crashes and routes fallback entries based on global demand indicators.

---
##  Execution Instructions

1. Run the system notebook cells inside the local directory pathway:
pip install numpy pandas scikit-learn

2. Open the file via VS Code Jupyter extension and execute cell by cell.

Submitted by Sadaf Ramzan.