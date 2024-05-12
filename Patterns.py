def generate_right_triangle():
    h= int(input("Enter the height of the triangle: "))
    for row in range(1, h + 1):
       for star in range(row):
        print("*", end='')
       print()

generate_right_triangle()