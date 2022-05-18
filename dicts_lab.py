
## Q1:Build a phone book program that receives the phone number, and returns the name of the owner. 
You can follow the table below:


contacts= {'Amal': '0531511811' ,'Mohammed': '0551511231', 
          'Khadijah':'0531511113','Abdullah':'0541511123',
          'Rawan': '0591511128','Faisal':'0581521129','Layla':'0563513453' }


search_num = input('Enter phone number:')

if len(search_num) !=10:
    print('This is invalid number')

elif not search_num.isnumeric:
    print('This is invalid number')

else:
    print('Sorry, the number is not found') 

name= [n for n, value in contacts.items() if value == search_num]
print(name)


## Q2:Write a function that receives a list containing different numbers ex: [23, 0, 873, 0, 14, 50, 0], 
# rearranges the list so that the zeros are the end of the list, and finally returns the arranged list.

def zero_last(my_list: list):
    ''' this function  rearranges the list so that the zeros are the end of the list'''
    my_list.sort(reverse=True)
    return my_list

numbers =[23, 0, 873, 0, 14, 50, 0]

print(zero_last(numbers))



