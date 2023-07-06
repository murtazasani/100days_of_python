# Program to Calculate BMI(Body Mass Index) of a Person in two ways.


do = input("Do You Want to Enter Height in Meters or Inches: ").capitalize()
if do == "Meters":
    height = float(input("Enter height in Meters: "))
    weight = float(input("Enter Weight in Kilograms: "))
    print("Height is:", height, "Meters.")
    print("Weight is:", weight, "Kilograms.")
    bmi = weight / (height * height)
    print("BMI is =", bmi)
elif do == "Inches":
    height = float(input("Enter height in Inches: "))
    weight = float(input("Enter Weight in Pounds: "))
    print("Height is:", height, "Inches.")
    print("Weight is:", weight, "Pounds.")
    bmi = (weight / (height * height)) * 703
    print("BMI is =", bmi)
else:
    print("You Enter the wrong Measurable Term. Please Enter Write Measurable Term")

if 'bmi' in locals():
    if float(bmi) < 18.5:
        print("BMI is less than 18.5. You are underweight.")
    elif float(bmi) >= 18.5 and bmi < 25:
        print("BMI is between 18.5 and 24.9. You have a healthy weight.")
    elif float(bmi) >= 25 and bmi < 30:
        print("BMI is between 25 and 29.9. You are overweight.")
    else:
        print("BMI is 30 or greater. You are obese.")