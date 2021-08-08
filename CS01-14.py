num_list = [5, 10, 15, 20, 25, 50, 20]

for i in range(len(num_list)):
    if num_list[i] == 5:
        num_list[i] = 10
    
    if num_list[i] == 10:
        num_list[i] = 15
    
    if num_list[i] == 15:
        num_list[i] = 20
    
    if num_list[i] == 20:
        num_list[i] = 25

    if num_list[i] == 25:
        num_list[i] = 50
    
    if num_list[i] == 50:
        num_list[i] = 200

print(num_list)