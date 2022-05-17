
telephone_guide= {
    "0531511811": 'Amal',
    "0551511231": 'Mohammed',
    "0531511113": 'Khadijah',
    "0541511123": 'Abdullah',
    "0591511128": 'Rawan',
    "0581521129": 'Faisal',
    "0563513453": 'Layla'
}

input_user= input("Enter the phone number: ")


if input_user in telephone_guide:
    print(telephone_guide[input_user])

elif len(input_user) < 10 or len(input_user) > 10 or not (input_user.isdigit()):
     print("This is invalid number")  

elif input_user not in telephone_guide:
    print("Sorry, the number is not found")


def zeros_right(nums_list:list = [23, 0, 873, 0, 14, 50, 0]):
    nums = []
    zeros = []
    for i in range(len(nums_list)):
        if nums_list[i] != 0:
            nums.append(nums_list[i])
        else:
            zeros.append(nums_list[i])
    nums.sort()        
    print('arranged list = ',nums+zeros)  

zeros_right()  
