try:
    width = float(input("Enter a rectangle width: "))
    length = float(input("Enter a ectangle length: "))

    if width == length:
        exit("That looks like a square.")

    area = width * length
    print(area)

except ValueError:
    print("Please enter a number.")