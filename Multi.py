n = int(input("Enter the number for which you want the multiplication table: "))
m = int(input("Enter the limit for the table: "))
i = 1

while i <= m:
    i += 1
    print(f"{n} * {i} = {n * i}")
    
    