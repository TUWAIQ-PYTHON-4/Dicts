'''phone_book = {"0531511811":"Amal","0551511231":"Mohammed","0531511113":"Khadijah","0541511123":"Abdullah","0591511128":"Rawan","0581521129":"Faisal","0563513453":"Layla"}
phone_number = str(input("enter the phone number: "))
#print(phone_book[input("enter the phone number: ")])

if len(phone_number) != 10:
    print("This is invalid number")
else:
    if phone_number.isdecimal() != False:
        if phone_number in phone_book:
            print(phone_book[phone_number])
        else:
            print("Sorry, the number is not found")
    else:
        print("This is invalid number")
'''
def list_of_numbers ():
    defult_list = [23, 0, 873, 0, 14, 50, 0]
    new_list =[]
    while len(defult_list) != 0:
        max_value = max(defult_list)
        defult_list.remove(max_value)
        new_list.append(max_value)
    print(new_list)
list_of_numbers()