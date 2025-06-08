# Lower Traingle
rows = int(input("Enter the number of rows of lower Traingle: "))
for i in range(rows):
    for j in range(i+1):
        print("*", end=" ")
    print()