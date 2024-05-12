h = int(input("Enter the height for the triangle: "))
for row in range(h):
    for star in range(row+1):
        print("*", end='')
    print()
    