
seasons = ("Winter", "Spring", "Summer", "Autumn")

month = int(input("Enter month number (1-12): "))

if month == 12 or month == 1 or month == 2:
    season = seasons[0]
elif month == 3 or month == 4 or month == 5:
    season = seasons[1]
elif month == 6 or month == 7 or month == 8:
    season = seasons[2]
elif month == 9 or month == 10 or month == 11:
    season = seasons[3]
else:
    season = "Invalid month"

print("Season is:", season)

names = set()

while True:
    name = input("Enter a name (empty to stop): ")

    if name == "":
        break

    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

print("Names entered:")

for n in names:
    print(n)
airports = {}

while True:
    print("1 = Enter new airport")
    print("2 = Fetch airport")
    print("3 = Quit")

    choice = input("Choose option: ")

    if choice == "1":
        icao = input("Enter ICAO code: ")
        name = input("Enter airport name: ")
        airports[icao] = name

    elif choice == "2":
        icao = input("Enter ICAO code: ")
        if icao in airports:
            print("Airport name:", airports[icao])
        else:
            print("Airport not found")

    elif choice == "3":
        break

    else:
        print("Invalid option")