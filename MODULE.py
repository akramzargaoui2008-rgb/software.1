


number = 1

while number <= 1000:
    if number % 3 == 0:
        print(number)
    number = number + 1


inches = float(input("Enter inches: "))


while inches >= 0:
    centimeters = inches * 2.54
    print(centimeters)
    inches = float(input("Enter inches: "))

    number = input("Enter a number: ")

    smallest = float(number)
    largest = float(number)

    number = input("Enter a number: ")

    while number != "":
        value = float(number)

        if value < smallest:
            smallest = value
        if value > largest:
            largest = value

        number = input("Enter a number: ")

    print(smallest)
    print(largest)



import random

secret = random.randint(1, 10)
guess = int(input("Guess a number: "))




while guess != secret:
    if guess < secret:
        print("Too low")
    if guess > secret:
        print("Too high")
    guess = int(input("Guess a number: "))

print("Correct")


attempts = 0

username = input("Username: ")
password = input("Password: ")



while attempts < 5 and (username != "python" or password != "rules"):
    attempts = attempts + 1
    username = input("Username: ")
    password = input("Password: ")



if username == "python" and password == "rules":
    print("Welcome")
else:
    print("Access denied")

    import random

    points = int(input("How many random points: "))
    count = 0
    inside = 0

    while count < points:
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x * x + y * y < 1:
            inside = inside + 1

        count = count + 1

    pi = 4 * inside / points
    print(pi)






