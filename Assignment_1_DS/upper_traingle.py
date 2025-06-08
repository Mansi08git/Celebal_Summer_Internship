# Upper Traingle
rows = int(input("Enter the number of rows of Upper Traingle: "))
for i in range(rows):
    for j in range(i, rows):
        print("*", end=" ")
    print()