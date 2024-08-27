# find the maximum number in each row of a 2D list and store the results in a seperate list

number_list = list()

for i in range(2):
    number_row = list()
    for j in range(2):
        number_row.append(int(input(f"Enter any number for index ({i+1}, {j+1}):")))
    number_list.append(number_row)
    
for row in number_list:
    print(row)
    
    
new_list = list()

for row in number_list:
        new_list.append(max(row))
    
print("The new list with maximum values:",new_list)