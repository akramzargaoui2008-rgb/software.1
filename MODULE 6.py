import random

def roll_dice():
    return random.randint(1, 6)

result = roll_dice()

while result != 6:
    print(result)
    result = roll_dice()

print(result)
import random

def roll_dice(sides):
    return random.randint(1, sides)

sides = int(input("Enter number of sides: "))

result = roll_dice(sides)

while result != sides:
    print(result)
    result = roll_dice(sides)

print(result)
def gallons_to_liters(gallons):
    return gallons * 3.785

gallons = float(input("Enter gallons: "))

while gallons >= 0:
    liters = gallons_to_liters(gallons)
    print("Liters:", liters)
    gallons = float(input("Enter gallons: "))
def sum_list(numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total

numbers = [1, 2, 3, 4, 5]
result = sum_list(numbers)

print("Sum:", result)
def even_numbers(numbers):
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n)
    return result

numbers = [1, 2, 3, 4, 5, 6]
new_numbers = even_numbers(numbers)

print("Original list:", numbers)
print("Even numbers:", new_numbers)
import math

def pizza_unit_price(diameter, price):
    radius = (diameter / 2) / 100
    area = math.pi * radius * radius
    return price / area

d1 = float(input("Enter diameter of pizza 1: "))
p1 = float(input("Enter price of pizza 1: "))

d2 = float(input("Enter diameter of pizza 2: "))
p2 = float(input("Enter price of pizza 2: "))

price1 = pizza_unit_price(d1, p1)
price2 = pizza_unit_price(d2, p2)

if price1 < price2:
    print("Pizza 1 is better value.")
else:
    print("Pizza 2 is better value.")
