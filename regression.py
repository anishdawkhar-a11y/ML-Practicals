import numpy as np
from sklearn.linear_model import LinearRegression

# Input: Study hours and practice hours
input_data = np.array([
    [2, 1],
    [3, 2],
    [4, 3],
    [5, 4],
    [6, 5]
])

# Output: Marks obtained
student_marks = np.array([30, 40, 50, 60, 70])

# Create and train the model
model = LinearRegression()
model.fit(input_data, student_marks)

# Predict marks for two new students
new_students = np.array([
    [7, 6],
    [8, 7]
])

predicted_marks = model.predict(new_students)

print("Student 1 Predicted Marks:", predicted_marks[0])
print("Student 2 Predicted Marks:", predicted_marks[1])
