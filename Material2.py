# TASK1
# name = "Maksym"
# age = 18
# gpa = 3.2
# is_student = True
# print(type(is_student) )



# TASK2
# name = "Maksym" # str
# age = 18 # int
# gpa = 3.2 # float
# is_student = True # bool

# gpa = int(gpa)
# print(gpa)

# age = float(age)
# print(age)

# name = bool(name)
# print(type(name))



# TASK3
# age = 18 # int
# age = str(age)

# age += "1"
# print(age)



# TASK4 
# Rectangle Area Calc
# length = float(input("Please eneter the length: "))
# width = float(input("Pplease enter the width: "))
# area = length * width 
# print (f"The area is: {area}cm^2")



# TASK5 
#x = 3.14
#y = -4
#z = 5

# result = round(x)
# result = max(x, y, z)
# result = min(x, y, z)
# result = pow(y, 3)
# result = abs(y)
# print(result)



# TASK6
# import math
# radius = float(input('Enter the radius of a circle: '))

# circumference = 2 * math.pi * radius

# print(f"The circumference is: {round(circumference, 2)}cm")



# TASK7
# import math

# a = float(input("Please enter the side A: "))
# b = float(input("Please enter the side B: "))
# c = math.sqrt(pow(a, 2) + pow(b, 2))

# print(f"Side C >>> {c}cm")



# TASK8
#unit = input("IS this temperature in Celsius or Fahrenheit (C/F): ")
#temp = float(input("PLease enter the temperature: "))

#if unit == "C" :  
#    temp = round((9 * temp) / 5 + 32, 1)
#    print(f"The temperature in Fahremheit is: {temp}^F")
#elif unit == "F" :
#    temp = round((temp - 32) * 5 / 9, 1)
#    print(f"The temperature in Celsius is: {temp}^C")
#else:
#    print(f"{unit} is an invalid unit if measurment")



# TASK9
temp = -5
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The ourdoor event is cancelled")
else: 
    print("The outdoor event is still scheduled")
    