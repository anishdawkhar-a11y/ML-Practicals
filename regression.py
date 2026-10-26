import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the student dataset
data = pd.read_csv("multivariate_linear_regression_data.csv")

# Input features and target
X = data[["Study_Hours", "Practice_Hours"]]
y = data["Student_Marks"]

# Train the multivariate linear regression model
model = LinearRegression()
model.fit(X, y)

# Predict marks
predicted = model.predict(X)

# Display actual and predicted marks
print("Actual vs Predicted Marks")
for actual, prediction in zip(y, predicted):
    print(f"Actual: {actual:.2f}, Predicted: {prediction:.2f}")

# Scatter plot: dots only
plt.figure(figsize=(8, 6))
plt.scatter(y, predicted, s=60)
plt.xlabel("Actual Student Marks")
plt.ylabel("Predicted Student Marks")
plt.title("Actual vs Predicted Student Marks")
plt.grid(True)
plt.tight_layout()
plt.show()
