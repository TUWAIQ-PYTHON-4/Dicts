def phone_guide():

    print ("Enter a number:")
    guide_number = input()

    numbers = {
        "0531511811":"Amal"
    ,"0551511231":"Mohammed"
    ,"0531511113":"Khadijah"
    ,"0541511123":"Abdullah"
    ,"0591511128":"Rawan"
    ,"0581521129":"Faisal"
    ,"0563513453":"Layla"
    }

    for key,value in numbers.items():
        if guide_number == value:
            print(key)
            return
    print("Sorry, the number is not found")
        elif guide_number != numbers:
            print("Sorry, the number is not found")
        else:
            print("This is invalid number")

phone_guide()

#q2
my_list=[23,0,873,0, 14, 50, 0]
for index, value in enumerate(my_list):
    if value == 0:
      my_list[index] = 9

print(my_list[:-1])