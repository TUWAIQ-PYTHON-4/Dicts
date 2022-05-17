dicts = {
    "Name": ["Amal" ,"Mohmmed","Khadijah","abdullah","Rawan","Faisal","Layla"] ,
    "Number": ['0531511811','0551511231','0531511113','0541511123','0591511128','0581521129','0563513453']
}

user_input=input("Enter the number :")
if not user_input.isdigit() :
    print("This is invalid number")
    


def fun_1():
    list_of_keys = [key
                    for key, list_of_values in dicts.items()
                    if user_input in list_of_values]
    if list_of_keys:                
        print(dict[user_input])
    else:
        print('Sorry, the number is not found')

#-------------------------
def fun_2():
    list_of_keys_2 = [key
                    for key, list_of_values_2 in dicts.items()
                    if int(user_input) >10 or int(user_input) <10 ]
    if list_of_keys_2:                
        print("This is invalid number")

fun_1()
fun_2()


