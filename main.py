phone_book = {"0531511811":"Amal","0551511231":"Mohammed","0531511113":"Khadijah","0541511123":"Abdullah","0591511128":"Rawan","0581521129":"Faisal","0563513453":"Layla"}

search_term = input("\nEnter the the phone number ")



if search_term !=10 and not search_term.isnumeric():
    print("This is invalid number")
elif search_term in phone_book:
    print(phone_book.get(search_term))    
else:
    print("Sorry, the number is not found")




a = [23, 0, 873, 0, 14, 50, 0]
temp = []
zeros = []

for i in range(len(a)):
    if a[i] !=0:
        temp.append(a[i])
    else:
        zeros.append(a[i])

print(temp+zeros)