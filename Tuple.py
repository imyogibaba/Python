print("Create a nested tuple and access and element inside the inner tuple.")
tup=(1,2,3,4,5)
print(tup)
nested=(11,22, (2,4,6,8) ,33,44,55)
print("Nested tuple:",nested)
print()
print("Inside the inner tuple:", nested[2][0])
print("Inside the inner tuple:", nested[2][1])
print("Inside the inner tuple:", nested[2][2])
print("Inside the inner tuple:", nested[2][3])



print("Convert a string into a tuple of characters.")
s=input("Enter a string")
conv=tuple(s)
print("After converting string into a tuple of characters",conv)


print("Find the maximum and minimum values in a tuple of numbers.")
tup=eval(input("Enter a tuple"))
print("Maximum value of this tuple is:", max(tup))
print("Minimum value of this tuple is:", min(tup))
print("\n")

print("Slice a tuple from index 2 to index5 and display the sub-tuple.")
a=eval(input("Enter a tuple"))
print("The sub-tuple from index 2 to 5 are:",a[2:6])


print("Write a program to iterate through a touple and print each element.")
tup=eval(input("Enter a tuple"))
print("The tuple list is:",tup)
print("\n")

print("Concatenate two tuples and display the result.")
a1=eval(input("Enter a tuple"))
a2=eval(input("Enter a tuple"))
print("The Concatente of tuple is:",a1+a2)
print("\n")


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

