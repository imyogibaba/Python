items=["Pen","Notebook","Shirt","Bottle","cap","Pencil"]
Rs=[10,40,200,250,120,5]
dict={"Pen":10 ,
            "Notebook":40 ,
              "Shirt":200 ,
              "Bottle":250 ,
              "Cap":120 ,
              "Pencil":5
}
print("keys fo dictionary are:", dict.keys())
print("Value of dictionary are:", dict.values())
print()
for i in dict.keys():
    print(i,"=Rs",dict[i])
print("\n")

#What is Dictionary?
#Definition:A dictionary is an unordered collection of data in key-value pairs.
#Declaration:Created using curly braces{}, with keys and corresponding values separated by colons:
print("WAP to count a sequence using insertion sort")
list=[15,6,13,6,33,85,3,48,24]
print("Oranginal list is:",list)
for i in range(1,len(list)):
    key=list[i]
    j=i-1
    while j>=0 and key<list[j]:

            list[j+1]=list[i]
            j=j-1
    else:
        list[j+1]=key
print("List after sorting:",list)
print("\n")

employee={'salary':10000,'age':24,'name':'john'}
print("\n")

print("Write a program to create a dictionary ocntaining names of competition winner students a keys and number of their wins as values.")
n=int(input("How many students?"))
CompWinners={}
for a in range(n):
    key=input("Name of the student:")
    value=int(input("Number of competitions won:"))
    CompWinners[key]=value
print("The dictionary now is:")
print(CompWinners)
print("\n")

