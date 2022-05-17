#Q1:Build a phone book program that receives the phone number, and returns the name of the owner.
phone_book = {"0531511811":"Amal" ,"0551511231":"Mohammed","0531511113":"Khadijah","0541511123":"Abdullah" , "0591511128":"Rawan","0581521129":"Faisal","0563513453":"Layla"}

#Ask the user to enter the phone number using input
phone_number = input("Enter the phone number: ")

#If the number is less or more than 10 numbers, print "This is invalid number".
if len(phone_number) < 10 or len(phone_number) > 10 :
    print("This is invalid number")

#If the number contains letters or symbols, print "This is invalid number".
if not phone_number.isdigit():
    print("This is invalid number")

#If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".

for key , value in phone_book.items():
    if key == phone_number:
        print(value)
        break
    else:
        continue
else:
    print("Sorry, the number is not found")


#Q2:Write a function that receives a list containing different numbers ex: [23, 0, 873, 0, 14, 50, 0], rearranges the list so that the zeros are the end of the list, and finally returns the arranged list.
def sort_zeros(num_list):
    num_list.sort(reverse=True)
    return print(num_list)

num_list = [23, 0, 873, 0, 14, 50, 0]
sort_zeros(num_list)









"""phone_book = {"Amal":"0531511811" ,"Mohammed":"0551511231","Khadijah":"0531511113","Abdullah":"0541511123" , "Rawan":"0591511128","Faisal":"0581521129","Layla":"0563513453"}
num = input("Enter the phone number: ")

if len(num) > 10 or len(num) < 10 :
    print("This is invalid number")
if num == num.isalpha():
    print("This is invalid number")

for k,v in phone_book.items():
    if v == num:
        print(k)
        break
else:
    print( "Sorry, the number is not found")


#Q2:Write a function that receives a list containing different numbers ex: [23, 0, 873, 0, 14, 50, 0], rearranges the list so that the zeros are the end of the list, and finally returns the arranged list.

def i():
    list=[23, 0, 873, 0, 14, 50, 0]
    list2=sorted(list)
    print(list2.reverse())

i()"""
"""         
def num_list(a=[]):
    s= a.sort(reversed) 

    return print(a)

num_list([23, 0, 873, 0, 14, 50, 0])

"""





    

"""keys = [k for k, v in phone_book.items() if v == num if (num > 10 or num <10 ) ]
print(keys)
"""
"""keys = [k for k, v in phone_book.items() if v is not num ]
print("Sorry, the number is not found")"""



"""if num in phone_book:
    print(phone_book[num]) 
else:
    print("Sorry, the number is not found")
"""
"""if num < 10 or num >10:
    print("This is invalid number")
"""


