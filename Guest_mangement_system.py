#Guest management list
guest_list=["honey singh","drake","kendric lamar","Divyansh"]
choise=0

print("++++++++++Diddy party list++++++++++")
print("Press 1 to check your name in list")
print("Press 2 to add your name in list")
print("Press 3 to  eleminate your name from list")

choise=int(input("Enter your choise ! "))

if choise==1:
 check_name=input("Enter the name : ")
 if check_name in guest_list:
   print("You are invited") 


elif choise==2:
 print("Name not found. Enter the name which you want to add!")
 name = input("Enter name: ")
 guest_list.append(name)
 print(f"You are invited now, congratulations!  \n Updated Guest List: {guest_list}") 

elif choise==3:
 print("Enter the name  which you want to eliminate ! :")
 name = input("Enter name: ")
 guest_list.remove(name)
 print(f"The  name is  eliminated ! uadated list : {guest_list}")
else:
 print("Invaild choise")