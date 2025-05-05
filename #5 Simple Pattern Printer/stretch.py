# Simple Pattern Printer

# Stretch Goal: Add inverted and pyramid pattern options.

rows = int(input("Enter the number of rows: "))
print("Choose a pattern:")
print("1. Triangle")
print("2. Inverted Triangle")
print("3. Pyramid")

choice = input("Enter 1, 2 or 3: ")

if choice == "1":
    for i in range(1, rows + 1):
        print("*" * i)

elif choice == "2":
    for i in range(rows, 0, -1):
        print("*" * i)

elif choice == "3":
    for i in range(1, rows + 1):
        spaces = ' ' * (rows - i)
        stars = '*' * (2 * (i))
        print(spaces + stars)

else:
    print("Invalid choice.")
