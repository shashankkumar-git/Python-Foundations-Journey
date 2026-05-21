#Task 1: Modify or rewrite your BMI function to handle both Metric (meters) and Imperial (inches) units.
#Name your function calculate_bmi_advanced(weight, height, system="metric").
#If system == "metric", use your current formula: weight / (height  2).
#If system == "imperial", the formula changes slightly: (weight / (height  2)) * 703.
#Test it once with metric inputs and once with imperial inputs (weight=150, height=68, system="imperial").


def calculate_bmi_advanced(weight, height, system):
    if system == "metric":
        return weight / height**2
    else:
        return (weight / (height**2)) * 703
    
data_1 = calculate_bmi_advanced(weight=150, height=68, system="imperial")
data_2 = calculate_bmi_advanced(weight=65, height=1.72, system="metric")


#Task 2: Create a secondary function called get_bmi_status(bmi).
# It should accept a numerical BMI value.
# Use if-elif-else inside to return a string:
# Below 18.5 --> "Underweight"
# 18.5 to 24.9 --> "Normal weight"
# 25 to 29.9 --> "Overweight"
# 30 or above --> "Obese"
# Bonus: Call your first function, save the result to a variable, and pass that variable directly into your second function to
# print the final status.


def get_bmi_status(bmi):
    if bmi < 18.5:
        return("Underweight")
    elif 18.5 < bmi < 24.9:
        return("Normal weight")
    elif 25 < bmi < 29.9:
        return("Overweight")
    else:
        return("Obese")


print(get_bmi_status(data_1))
print(get_bmi_status(data_2))
