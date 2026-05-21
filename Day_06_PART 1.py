#PROBLEM STATEMENT - 1. Write a function called calculate_bmi that takes weight and height as parameters.
#                    2. It should return the BMI using the formula: weight / (height  2).
#                    3. Call the function and print the result.


def calculate_bmi(weight, height):
    return weight / height**2

print(calculate_bmi(65, 1.72))