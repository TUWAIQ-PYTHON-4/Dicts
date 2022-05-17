
def fun_1():
    my_list=[55,28,0,5848,0,11,0]
    n=len(my_list)
    count=0
    for i in range(n):
        if my_list[i] != 0:
            my_list[count] = my_list[i]
            count+=1

    while count < n:
        my_list[count] = 0
        count += 1
    print(my_list)

fun_1()    




