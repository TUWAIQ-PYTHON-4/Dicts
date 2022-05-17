## Q1:Build a phone book program that receives the phone number, and returns the name of the owner. 

concats={'Amal':'0531511811', 'Mohammed':'0551511231', 'Khadijah':'0531511113'}

user_input=input('Enter the phone number: ')

if user_input in concats.values():
    keys = [k for k, v in concats.items() if v == user_input]
    print(keys)

elif len(user_input) < 10 or len(user_input) > 10:
     print('This is invalid number, enter only 10 digits')

elif  not(user_input.isdigit()):
    print('This is invalid phone number, enter only digits')

else:
    print('Sorry, the number is not found') 


## Q2:Write a function that receives a list containing different numbers
#  ex: [23, 0, 873, 0, 14, 50, 0], rearranges the list so that the zeros are the end of the list,
#  and finally returns the arranged list.

def my_list(nums_list:list) -> list:
    nums = []
    zeros = []
    for i in range(len(nums_list)):
        if nums_list[i] != 0:
            nums.append(nums_list[i])
        else:
            zeros.append(nums_list[i])
    nums.sort()        
    print('arranged list = ',nums+zeros)  


my_list([23, 0, 873, 0, 14, 50, 0])      
