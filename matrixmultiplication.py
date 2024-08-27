# multiply 2D lists (matrices) of size 3 by 3 

num = int(input("Enter the size of your matrix:"))

matrix1 = list()

for i in range(num):
    row_list1 = list()
    for j in range(num):
        row_list1.append(int(input(f"Enter any number for ({i+1}, {j+1})")))
    matrix1.append(row_list1)

matrix2 = list()

for i in range(num):
    row_list2 = list()
    for j in range(num):
        row_list2.append(int(input(f"Enter any number for ({i+1}, {j+1})")))
    matrix2.append(row_list2)
    
result = [[0 for _ in range(num)] for _ in range(num)]

for i in range(num):
    for j in range(num):
        for k in range(num):
            result[i][j] += matrix1[i][k] * matrix2[k][j]
   

print("The result is:")
for row in result:
    print(row)
    