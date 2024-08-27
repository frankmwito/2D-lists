# transpose a 2D list - convert rows to columns and vice versa

matrix = []

for i in range(3):
    row = []
    for j in range(3):
        number = int(input(f"Enter a member for position ({i+1}, {j+1}):"))
        row.append(number)
    matrix.append(row)

print("original matrix:")
    
for row in matrix:
    print(row)

transposed_matrix = []
    
for i in range(3):
    transposed_row = list()
    for j in range(3):
        transposed_row.append(matrix[j][i])
    transposed_matrix.append(transposed_row)
    
print("\ntransposed matrix")
for row in transposed_matrix:
    print(row)
