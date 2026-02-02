import random

dice_count = int(input("How many dice do you want to roll? "))

total = 0

for i in range(dice_count):
    roll = random.randint(1, 6)
    total = total + roll

print("Sum of dice:", total)
numbers = []

value = input("Enter a number: ")

while value != "":
    numbers.append(int(value))
    value = input("Enter a number: ")

numbers.sort(reverse=True)

print("Five greatest numbers:")
for n in numbers[:5]:
    print(n)
number = int(input("Enter an integer: "))

is_prime = True

if number < 2:
    is_prime = False
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False

if is_prime:
    print("The number is prime.")
else:
    print("The number is not prime.")
cities = []

for i in range(5):
    city = input("Enter a city name: ")
    cities.append(city)

for city in cities:
    print(city)

