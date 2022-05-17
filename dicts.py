
'''
 Q1:Build a phone book program that receives the phone number.
 and returns the name of the owner. 
'''
phone_dict = {'0531511811':'Amal' ,
               '0551511231':'Mohammed' ,
              '0531511113':'Khadijah' ,
             '0541511123' :'Abdullah' ,
            '0591511128' : 'Rawan' ,
             '0581521129': 'Faisal' ,
              '0563513453':'Layla' , }

phone_num = input('Enter a phone numbear: ')
try:
    if phone_num.isdecimal() and len(phone_num) == 10:
       print( phone_dict[phone_num])
    else:
       print("This is invalid number")
except: print("Sorry, the number is not found")

'''
 Q2:Write a function that receives a list containing different numbers 
 ex: [23, 0, 873, 0, 14, 50, 0], rearranges the list so that 
 the zeros are the end of the list, and finally returns the arranged list.
'''

def zeros_to_end(arr: list = [23, 0, 873, 0, 14, 50, 0]) -> list:
    n = arr.count(0)
    for i in range(n):
          arr.remove(0)
    for i in range(n):
          arr.append(0)

    return arr

print(zeros_to_end())   
