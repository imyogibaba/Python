
#Grocery List Manager
#Write a program that allows a user to add items to a grocery list (list of strings). Print the final list after the user enters "done"

#Answer:

#grocery list manager
print("This program manages your grocery")
print("="*20)
print("GROCERY MANAGER - FUNCTIONS")
print("1. Add new items \n2. Remove items \n3.Show List")
choice="y"
list1=[]  #empty list
while choice=="y":
  option=int(input("\nSelect your operation(1,2,3): "))
  if option==1:   #add new items
    print("\n__ ADD NEW ITEMS __ ")
    num=eval(input("Enter the items you want to add: "))
    list1.extend(num)
    print(">> Items have been saved!")
  elif option==2:
    print("\n__ REMOVE ITEMS __")
    ele=input("Which item you want to remove?")
    list1.remove(ele)

    print(">> Item has been removed!")
  elif option==3:
    print("\n__ SHOW LIST __") #traversing
    for i in range(0, len(list1)):
      print(i+1,"-",list1[i])
  else:
    print("__ ERROR: OPERATION NOT FOUND __")
  choice=input("\nDo you want to continue (y/n)?")
    
print("\n ** PROGRAM ENDS HERE **\n")

#movie playlist

#Favourite Movie Manager
#Write a program that allows a user to add movies  (list of strings). Print the final list after the user enters "done"


#ANswer:

#grocery list manager
print("This program manages your favourite movies")
print("="*20)
print("MOVIE MANAGER - FUNCTIONS")
print("1. Add favourite movies \n2. Remove movie \n3.Display movies")
choice="y"
list1=[]  #empty list
while choice=="y":
  option=int(input("\nSelect your operation(1,2,3): "))
  if option==1:   #add new items
    print("\n__ ADD YOUR FAVOURITE MOVIE __ ")
    num=eval(input("Enter the movie you want to add: "))
    list1.extend(num)
    print(">> Movies have been saved!")
  elif option==2:
    print("\n__ REMOVE MOVIES __")
    ele=input("Which movie you want to remove?")
    list1.remove(ele)
    print(">> The movie has been removed!")
  elif option==3:
    print("\n__ DISPLAY MOVIE __") #traversing
    for i in range(0, len(list1)):
      print(i+1,"-",list1[i])
  else:
    print("__ ERROR: OPERATION NOT FOUND __")
  choice=input("\nDo you want to continue (y/n)?")
    
print("\n ** PROGRAM ENDS HERE **\n")

