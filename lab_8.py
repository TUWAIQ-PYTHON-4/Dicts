#Q1:Build a phone book program that receives the phone number, and returns the name of the owner.

phone_book = {"Amal":"0531511811" ,"Mohammed":"0551511231","Khadijah":"0531511113","Abdullah":"0541511123" , "Rawan":"0591511128","Faisal":"0581521129","Layla":"0563513453"}
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

i()
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


