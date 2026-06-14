# DecodeLabs AI Internship - Week 2 Project
# Done by: Sadaf Ramzan

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

print(" Iris Data Classification Setup ---")

# Step 1: Loading the dataset

raw_data = load_iris()
X = pd.DataFrame(raw_data.data, columns=raw_data.feature_names)
y = raw_data.target

print(f" Dataset loaded successfully with {X.shape[0]} samples.")

# Step 2: Splitting data into 80% training and 20% testing

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)
print(f" Train-Test Split done (80/20 ratio).")

# Step 3: Scaling features using StandardScaler

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print("Data normalization/scaling applied.")

# Step 4: Beyond Requirements - Tuning K value using Elbow Method

print(" Finding the best K value using Error Rates...")
error_rates = []

for k in range(1, 21):
    test_knn = KNeighborsClassifier(n_neighbors=k)
    test_knn.fit(X_train_scaled, y_train)
    predictions_test = test_knn.predict(X_test_scaled)
    error_rates.append(np.mean(predictions_test != y_test))

# Automatically choosing the K with minimum error rate
best_k = range(1, 21)[np.argmin(error_rates)]
# Making sure K is odd to avoid voting ties
if best_k % 2 == 0:
    best_k += 1

print(f" Optimal K selected for this dataset: K = {best_k}")

# Step 5: Training final model with the best K
final_model = KNeighborsClassifier(n_neighbors=best_k)
final_model.fit(X_train_scaled, y_train)
final_predictions = final_model.predict(X_test_scaled)

# Step 6: Printing Final Results & Evaluation Metrics
print("\n" + "="*40)
print(" MODEL PERFORMANCE REPORT")
print("="*40)

accuracy = accuracy_score(y_test, final_predictions)
print(f"System Accuracy: {accuracy * 100:.2f}%")

print("\n Confusion Matrix Table:")
print(confusion_matrix(y_test, final_predictions))

print("\n Complete Classification Blueprint:")
print(classification_report(y_test, final_predictions, target_names=raw_data.target_names))
print("="*40)

# Saving the elbow method graph locally
plt.figure(figsize=(8, 4))
plt.plot(range(1, 21), error_rates, color='purple', linestyle='dashed', marker='o', markerfacecolor='yellow')
plt.title('Elbow Method: Error Rate vs K Value')
plt.xlabel('K Value')
plt.ylabel('Error Rate')
plt.grid(True)
plt.savefig('k_value_optimization.png')
print("\n Optimization plot saved as 'k_value_optimization.png'. Process finished.")