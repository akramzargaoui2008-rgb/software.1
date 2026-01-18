
user = input('Enter your name: ')
print("Hello, " + user + "!")



import math

radius_str = input("Enter the radius of the circle: ")
radius = float(radius_str)
area = math.pi * radius ** 2
print(f"The area of the circle is {area}")

length_str = input("Enter the length of the rectangle: ")
length = float(length_str)
width_str = input("Enter the width of the rectangle: ")
width = float(width_str)
perimeter = 2 * (length + width)
area = perimeter * width
print(f"The perimeter of the rectangle is {perimeter}")
print(f"The area of the rectangle is {area}")


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
sum = num1 + num2 + num3
product = num1 * num2 * num3
average = sum / 3
print(f"The sum of the three numbers is {sum}")
print(f"The product of the three numbers is {product}")
print(f"The average of the three numbers is {average}")


pounds_strings = input("Enter the mass in pounds: ")
lots_strings = input("Enter the mass in lots: ")
talents_strings = input("Enter the mass in tale: ")
talent_conversion_grams =float(talents_strings) * 20 * 32 * 13.3
pound_conversion_grams =float(pounds_strings) * 32
lot_conversion_grams =float(lots_strings) * 13.3

sum_kilograms = (talent_conversion_grams + pound_conversion_grams + lot_conversion_grams) / 1000


print(f"The weight in modern units : {sum_kilograms}")


import random

digit_three_1 = random.randint(0,9)
digit_three_2 = random.randint(0,9)
digit_three_3 = random.randint(0,9)

digit_four_1 = random.randint(0,6)
digit_four_2 = random.randint(0,6)
digit_four_3 = random.randint(0,6)
digit_four_4 = random.randint(0,6)
digit_five_1 = random.randint(0,6)


print(f"3-digit code:\n {digit_three_1}{digit_three_2}{digit_three_3}")
print("3-digit code: " +str(digit_three_1) + str(digit_three_2) + str(digit_three_3))
print(f"4-digit code:\n {digit_four_1}{digit_four_2}{digit_four_3}{digit_four_4}")
