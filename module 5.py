import random

dice_count = int(input("How many dice do you want to roll? "))

total = 0

for i in range(dice_count):
    roll = random.randint(1, 6)
    total += roll

print("The sum of the dice is:", total)
numbers = []

value = input("Enter a number (empty to quit): ")
while value != "":
    numbers.append(int(value))
    value = input("Enter a number (empty to quit): ")

numbers.sort(reverse=True)

print("Five greatest numbers:")
for num in numbers[:5]:
    print(num)
number = int(input("Enter an integer: "))

is_prime = True

if number < 2:
    is_prime = False
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")
cities = []

for i in range(5):
    city = input("Enter the name of a city: ")
    cities.append(city)

print("Cities entered:")
for city in cities:
    print(city)
