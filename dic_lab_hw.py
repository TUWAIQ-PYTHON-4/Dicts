phone_dic={'531511811':"Amal" ,  '551511231':"Mohammed", '531511113' :"Khadijah"
,  '541511123':"Abdullah",'591511128':'Rawan','581521129':'Faisal','563513453':'Layla'}

phone_num = input("please Enter a Phone Number")
if phone_num in phone_dic:
  print(phone_dic.get(phone_num))
elif phone_num != 10 or not phone_num.isnumeric():
  print("This is invalid number")
else:
 print("Sorry, the number is not found")

def num_list():
  list1=[1,22,0,9,0]
  list2=[]
  while len(list1)!=0:
    max_num = max(list1)
    list1.remove(max_num)
    list2.append(max_num)
    print(list2)

num_list() 