

print("Check whether a particular element exists in a tuple or not.")
a=eval(input("Enter a tuple"))
ele=eval(input("Enter a element you want to find"))
if ele in a:
        print("True")
else:
        print("False")


#Find the length of a tuple using len().
a=eval(input("Enter the tuple"))
print("The length of the tuple is:",len(a))


#Access the first and last elements of a tuple.
tup=eval(input("Enter your tuple"))
print("The first element of your tuple is:",tup[0])
print("The last element of your tuple is:", tup[-1])

#Convert a list into a tuple using tuple() and display the result.
list=eval(input("Enter a list"))
b=tuple(list)
print(b)



tup=eval(input("Enter a tuple:"))
tup2=(2,3,4,5,6,7,8,0)
print("Your tuple1:",tup)
print("Your tuple2:",tup2)
print("Length:",len(tup))
print("Maximum value:",max(tup))
print("Minimum value:",min(tup))
print("Occurange of 2 in tuple:", tup.count(2))
print("Concatenation of 2 tuples:", tup+tup2)
#replication
print("Replication of tup",tup*2)
#indexing
print("Replication",tup[2])
#slicing
print("Slicing",tup[0:2:11])
#del statement

#Create a tuple with five different fruits and print it.
list1=["apple","banana","mango","guava"]
print("list=",list1)
list1=tuple(list1)
print("after conversion", list1)






#Count the number of times a specific element appears in a tuple.
a=eval(input("Enter a tuple"))
b=eval(input("Enter the element you want to count"))

