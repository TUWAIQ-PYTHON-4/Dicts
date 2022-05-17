dict_phone = { "0531511811" :"Amal" ,  "0551511231" : "Mohammed" ,  "0531511113" :"Khadijah"  
,  "0541511123" : "Abdullah"  ,  "0591511128" : "Rawan" ,  "0581521129" : "Faisal" ,  "0563513453" : "Layla" }

phone_num = input ( " inter your number " )

if  len(phone_num) != 10 or not phone_num.isnumeric:

   print("This is invalid number")

elif phone_num in dict_phone.keys()  :
    print(dict_phone.get(phone_num))

 
else :
    print("Sorry, the number is not found")

# Q2

def arrang_function(arr: list = [23, 0, 873, 0, 14, 50, 0]) -> list:
    n = arr.count(0)
    for i in range(n):
          arr.remove(0)
    for i in range(n):
          arr.append(0)

    return arr

print(arrang_function())   
