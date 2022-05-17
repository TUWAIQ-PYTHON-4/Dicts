# Dicts


## Q1:Build a phone book program that receives the phone number, and returns the name of the owner. 
# If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
# If the number is less or more than 10 numbers, print "This is invalid number".
# If the number contains letters or symbols, print "This is invalid number".

phone_book_dict = {"Name":"Number",
                    "Amal":"0531511811",
                    "Mohammed":"0551511231",
                    "Khadijah":"0531511113",
                    "Abdullah":"0541511123",
                    "Rawan":"0591511128",
                    "Faisal":"0581521129",
                    "Layla":"0563513453"}


# Ask the user to enter the phone number using input
number = input("Please Enter a Phonenumber .. ")
counter = 0
# letter ans symbol counter 
other_counter = 0

for i in number:
    if i.isdigit():
        counter += 1
    else:
        other_counter +=1
        break
if (counter < 10 or counter >10) or other_counter > 0:
    print("This is invalid number")
else: 
    for x, y in phone_book_dict.items():
        if number == y:
            print("This phone number belongs to {}".format(x))
            break
    else:
        print("Sorry, the number is not found")
    
        
    
    


## Q2:Write a function that receives a list containing different numbers 
# ex: [23, 0, 873, 0, 14, 50, 0], rearranges the list so that the zeros are the end of the list, 
# and finally returns the arranged list.

def shift_zeroz(new_list):

    '''
    The shift_zeroz receives a list containing different numbers 
    rearranges the list so that the zeros are the end of the list, 
    and finally returns the arranged list.
    '''
    zeroz_list = [0 for i in range(new_list.count(0))]
    shifted_list = [i for i in new_list if i != 0]
    shifted_list.extend(zeroz_list)
    return shifted_list

shift_zeroz([1,2,4,6,0,1,2,0,1,0,0,1])