'''
## Q1:Build a phone book program that receives the phone number, and returns the name of the owner. 
You can follow the table below:

| Name    | Number      |
| -------- | ---------- |
| Amal     | 0531511811 |
| Mohammed | 0551511231 |
| Khadijah | 0531511113 |
| Abdullah  | 0541511123 |
| Rawan    | 0591511128 |
| Faisal   | 0581521129 |
| Layla    | 0563513453 |


- Ask the user to enter the phone number using input
- If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
- If the number is less or more than 10 numbers, print "This is invalid number".
- If the number contains letters or symbols, print "This is invalid number".
'''


phone_book={"amal":"0563513453","noura":"0581521129","sara":"0591511128"}
#Ask the user to enter the phone number using input
ask_user=input("Enter plase phone number :")
#If the number is less or more than 10 numbers, print "This is invalid number".
if len(ask_user)<10 or len(ask_user)>10:
    print("This is invalid number")
#If the number contains letters or symbols, print "This is invalid number".
if not ask_user.strip().isdigit():
    print("This is invalid number")
#If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
list_of_keys = [key for key, list_of_values in phone_book.items() if str(ask_user) in list_of_values]
if list_of_keys:
    print(list_of_keys)
else:
    print('Sorry, the number is not found')

#Q2:Write a function that receives a list containing different numbers ex: [23, 0, 873, 0, 14, 50, 0], rearranges the list so that the zeros are the end of the list, and finally returns the arranged list.
def list_number():
    list1= [23, 0, 873, 0, 14, 50, 0]
    list2=sorted(list1)
    print(list2)

list_number()


