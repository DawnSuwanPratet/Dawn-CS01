def my_list(num):
    for i in range(len(num)):
        if num[i] == 20:
            num[i] = 200
    
    print(num)

my_num = [5, 10, 20, 25, 50, 20, 15, 20]

my_list(my_num)