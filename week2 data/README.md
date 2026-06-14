# Week 2 Project: Data Classification using KNN

This folder contains my submission for Project 2 under the DecodeLabs AI Engineering Internship track. The goal of this task was to move away from hardcoded if-else statements and build a machine learning pipeline that learns patterns directly from data.

##  Project Flow & Implementation Details

### 1. Dataset Selection
* I used the classic Iris Dataset which has 150 instances spread across 3 unique categories (Setosa, Versicolor, and Virginica).
* The model takes 4 features into account: Sepal Length, Sepal Width, Petal Length, and Petal Width.

### 2. Core Engineering Steps
* Data Splitting: Divided the whole dataset into an 80% training set and a 20% testing set to keep the validation fair. I used stratify to make sure classes remain balanced in both sets.
* Feature Scaling: Applied StandardScaler to ensure all measurement units are properly normalized (Mean=0, Variance=1) so no single big value dominates the model logic.
* Beyond Requirements (Hyperparameter Optimization): Instead of picking a random value for K, I coded the Elbow Method to check error loops from K=1 to K=20. The script finds the exact point where the error drops and picks that optimal K automatically.

### 3. Model Results & Metrics
To confirm the output isn't hallucinating, the pipeline prints:
* Accuracy Score: Shows the overall correctness percentage of the predictions.
* Confusion Matrix: Breaks down the True Positives, False Alarms (Type I), and Missed Detections (Type II).

---
##  How to Run the Code

1. Make sure you have python libraries installed:
pip install numpy pandas scikit-learn matplotlib

2. Run the script directly through your VS Code terminal:
python app.py

Submitted by Sadaf Ramzan.