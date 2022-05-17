#the question one
def found_phone_number(PhoneNumber):
    for item in value_list:
        if item == int(PhoneNumber):
            TheIndex = value_list.index(int(PhoneNumber))
            return key_list[TheIndex]

    return "Sorry, the number is not found"

test_dict = {'amal' : 531511811 , 'mohammed' : 551511231 , 'khadijah' : 531511113 , 'abdillah' : 541511123 , 'rawan' : 591511128 , 'faisal' : 581521129 , 'layla' : 563513453}
key_list = list(test_dict.keys())
value_list = list(test_dict.values())
PhoneNumber = input("enter the phone number whithout zero")

if len(PhoneNumber) < 9 :
        print("This is invalid number")
elif not PhoneNumber.isdigit() :
        print("This is invalid number")
else:
    print(found_phone_number(PhoneNumber))

#the question two

def rearranges_the_list(list):
    list.sort()
    count = 0
    for i in list:
        if i != 0:
            list[count] = i
            count = count + 1

    for i in range(count, len(list)):
        list[i] = 0

list = [1,0,2,0,3,0,3]
rearranges_the_list(list)
print(list)