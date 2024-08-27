# 2D list representing a 3*3 matrix 

matrix = []

for i in range(3):
    row = []
    for j in range(3):
        number = int(input(f"Enter a member for position ({i+1}, {j+1}):"))
        row.append(number)
    matrix.append(row)
    
for row in matrix:
    print(row)
        