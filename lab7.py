import numbers

def c (arr):
    r=False
    for character in arr:
         is_letter = character.isalpha()
         if is_letter==True:
             r=True
             break
    return r

my_dict = {"0531511811":"Amal" ,"0551511231":"Mohammed"}
number=input("plz select phone number :  ")

if len(number)!=10 or c(number) ==True :
    print("This is invalid number")
elif number not in my_dict:
    print("Sorry, the number is not found")
else:
    print(my_dict.get(number))
    
def Zero(numberList):
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
Zero( [23, 0, 873, 0, 14, 50, 0])


