# calculate the sum of all elements in a 2D list

matrix = []

for i in range(3):
    row = []
    for j in range(3):
        number = int(input(f"Enter any number ({i+1}, {j+1}):"))
        row.append(number)
    matrix.append(row)
    

total_sum = 0

for row in matrix:
    for element in row:
        total_sum += element
        
        
        
print(f"The sum of all elements in the matrix is: {total_sum}")