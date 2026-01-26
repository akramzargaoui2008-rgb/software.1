"""rounds = int(input("Enter the number of rounds: "))

finiched_rounds = 0

while finiched_rounds < rounds:
    print("bonjour!!")
    finiched_rounds = finiched_rounds + 1

    command = input("Enter command:")
    while command !="stop":
        print("Executing command:" + command)
        command = input("Enter command:")
        print("Execution stopped")"""
"""command = input("Enter password:")
while command != "python123":
    print("incorrect password")
    password = input("Enter password:")
print("execution stopped")"""
"""import random
dice1 = dice2 = rolls = 0
while dice1!=6 and dice2!=0:

     dice1 = random.randint(1,6)
     dice2 = random.randint(1,6)
     rolls = rolls + 1
     
print(f"Rolled {rolls:d} times.")"""

""""first=1
second=1
while second<=5:
    print(f"{first} times {second} is {first*second}:d")
    first=first+1
    second=second+1"""

"""import random
rounds =0
while rounds <= 100000:
    dice1 = dice2 = rolls = 0
    while dice1!=6 or dice2!=0:
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        rolls = rolls + 1
        total_rolls = total_rolls + rolls
        average = total_rolls/2
        print(f"Average rolls required: {average:6.2f}")"""


command = input("Enter command:")
while command !="stop":
            if command == "MAYDAY":
                break
            print("Executing command:" + command)
            command = input("Enter command:")
else:
    print("Thank you for your time")
    print("execution stopped.")













