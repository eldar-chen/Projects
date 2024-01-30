# 1st input: enter height in meters e.g: 1.65
height = input('What is your height?: \n')
# 2nd input: enter weight in kilograms e.g: 72
weight = input('What is your weight?: \n')

height_ = float(height)
weight_ = float(weight)
bmi = weight_ / (height_*height_)
bmi_ = int(bmi)

print("You'r BMI is: ", bmi_)