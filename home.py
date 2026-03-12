# Task 1: Ask user input and print it
# name = input("What is your name? ")
# weight = float(input("What is your weight in kg? "))
# height = float(input("What is your height in meters? "))
# print("Your name is " + name + "\nyour weight is " + str(weight) + " kg and, \nyour height is " + str(height) + " meters.")

# print weight and height data types using type(). 
# print("The data type of weight is: " + str(type(weight)))
# print("The data type of height is: " + str(type(height)))

# Calculate BMI
# bmi = weight / (height * height)

# Print BMI result
# print("Your BMI is: " + str(bmi))

# Display formatted BMI report
# print("\n------ BMI REPORT ------")
# print("Name   :", name)
# print("Weight :", weight, "kg")
# print("Height :", height, "m")
# print("BMI    :", round(bmi, 2))
# print("------------------------")


# Day 3: Tasks
# Task 1: Create a function calculate_bmi(weight, height) that returns BMI.
def calculate_bmi(weight, height):
    bmi = weight / (height * height)
    return bmi
calculated_bmi = calculate_bmi(4, 1.75)
print("Your BMI is:", round(calculated_bmi, 2))