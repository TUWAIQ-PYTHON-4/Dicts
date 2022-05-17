


'''
phone_book={"0531511811":"Asma","0551511231":"Aml","0531511113":"hend","0541511123":"abdullah"}
phone_num=input("enter your phone number:")
if phone_num !=10 or not phone_num.isnumeric:
    print("invalid number")
elif phone_num in phone_book:
    print(phone_book.get(phone_num))
else:
    print("Sorry, the number is not found")
'''
def list_of_num():
    list1=[23, 0, 873, 0, 14, 50, 0]
    list2=[]
    while len(list1) !=0:
        max_number = max(list1)
        list1.remove(max_number)
        list2.append(max_number)
    print(list2)

list_of_num()