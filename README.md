# ML Practicals

This repository contains machine learning practicals implemented in Python.

## Practical 1: Multivariate Linear Regression

### Aim
To implement Multivariate Linear Regression using Python and predict student marks.

### Theory
Multivariate Linear Regression is a supervised machine learning algorithm used to predict a numerical value using two or more input variables.

In this practical:
- **Input variables:** Study hours and practice hours
- **Output variable:** Student marks

### Formula
```
Y = b0 + b1X1 + b2X2
```

Where:
- `Y` is the predicted value
- `b0` is the intercept
- `X1` and `X2` are input variables
- `b1` and `b2` are model coefficients

### Algorithm
1. Import NumPy and LinearRegression.
2. Create the input data and output marks.
3. Create a Linear Regression model.
4. Train the model using `fit()`.
5. Use `predict()` to predict marks for new students.
6. Display the predicted marks.

### Requirements
- Python 3
- NumPy
- scikit-learn

### Installation
Install the required libraries:

```bash
pip install -r requirements.txt
```

### Run the Program
Run this command in the terminal:

```bash
python regression.py
```

### Expected Output
```text
Student 1 Predicted Marks: 80.0
Student 2 Predicted Marks: 90.0
```

### Result
Thus, the Multivariate Linear Regression model was implemented successfully in Python to predict student marks using study hours and practice hours.
