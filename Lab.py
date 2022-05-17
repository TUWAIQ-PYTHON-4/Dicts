phoneBook={"0531511811": 'Amal', "0551511231":'Mohammed', "0531511113":'Khadijah', 
"0541511123":'Abdullah', "0591511128":'Rawan', "0581521129":'Faisal', "0563513453":'Layla'}
phoneNum=input("Enter Phone Number: ")
if phoneNum in phoneBook:
    print(phoneBook.get(phoneNum))
elif phoneNum != 10 or not phoneNum.isnumeric:
    print("This is invalid number")
else:
    print("Sorry, the number is not found")

def moveZero(numberList):
    n = len(numberList)
    count = 0
    for i in numberList:
      if i != 0:
        numberList[count] = i
        count += 1
    while count < n:
     numberList[count] = 0
     count += 1
    print(numberList) 
    
moveZero([23, 0, 873, 0, 14, 50, 0])
