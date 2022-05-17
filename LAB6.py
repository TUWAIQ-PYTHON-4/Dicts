# Q1:Build a phone book program that receives the phone number, and returns the name of the owner.
from multiprocessing.sharedctypes import Value

name_n0_dict = {"0531511811" : "Amal" , "0551511231" : "Mohammed" , "0531511113" : "Khadijah" , "0541511123" : "Abdullah" , "0591511128" : "Rawan" , "0581521129" : "Faisal" , "0563513453" : "Layla"}
  
    # Ask the user to enter the phone number using input
phone_num=input("enter the phone number")

    # If the number exists, print the owner. 
if phone_num in name_n0_dict:
    print(name_n0_dict[phone_num])

    # If the number is less or more than 10 numbers, print "This is invalid number".
elif(len(phone_num) < 10 or len(phone_num) > 10):
    print("This is invalid number")    

    # If the number contains letters or symbols, print "This is invalid number".
elif  phone_num.isnumeric !=True:
    print("This is invalid number!!") 

    # Otherwise, print "Sorry, the number is not found".  
else:
    print("Sorry, the number is not found")        

# Q2:Write a function that receives a list containing different numbers ex: [23, 0, 873, 0, 14, 50, 0], rearranges the list so that the zeros are the end of the list, and finally returns the arranged list.

def order_list(the_list:list):
  the_list.sort()
  print(the_list)

order_list([23, 0, 873, 0, 14, 50, 0])