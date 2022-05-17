'''
 Q1:Build a phone book program that receives the phone number, and returns the name of the owner.
'''

def phone_book():
    book_dict={"Amal":"0531511811", "Mohammed":"0551511231", "Khadijah":"0531511113", "Abdullah":"0541511123", "Rawan":"0591511128", "Faisal":"0581521129", "Layla":"0563513453"}
    #Ask the user to enter the phone number using input
    phone_number= input("Enter the phone number to find its owner: ")
    if len(phone_number)<10 or len(phone_number)>10:
        print("This is invalid number")
    elif phone_number.isnumeric() == False:
        print("This is invalid number")
    else:
        for key in book_dict:
            if phone_number==book_dict[key]:
                 print(key)
                 break
        else:
            print("Sorry, the number is not found")

 
# calling the phone book program
phone_book()

'''
Q2:Write a function that receives a list containing different numbers ex: [23, 0, 873, 0, 14, 50, 0],
rearranges the list so that the zeros are the end of the list, 
and finally returns the arranged list.
'''
def arrange_list(my_list):
    new_list=[]
    counter_of_zero=0
    # adding other numbers to a new list
    for num in my_list:
        if num != 0:
            new_list.append(num)
        else:
            counter_of_zero+=1
    # adding zeros that we skiped to the end of the list
    while counter_of_zero!=0:
        new_list.append(0)
        counter_of_zero-=1
    return new_list
# testing the function
any_list=[23, 0, 873, 0, 14, 50, 0]
print(arrange_list(any_list))

