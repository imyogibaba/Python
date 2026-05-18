print("WAP that counts the number of consonants and vowels in a string.")
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for char in text:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)
print()

print("Write a program to find the largest number among the other two.")
a=int(input("Enter the first no:"))
b=int(input("Enter the second no:"))
c=int(input("Enter the third no:"))
if a>b and a>c:
  print(a, "is the largest")
  print()
elif b>c and b>c:
  print(b,"is the largest")
  print()
elif c>a and c>b:
  print(c, "is the largest.")
  print()
else:
  print("all are same")
print()

print("Write a program to print all numbers from 1 to 10 using a loop")
for i in range(1,11):
  print(i)
print()

#Write a Python program to find the square of a number.
print("This is a program in which we will find the square of the given number by the user.")
a=int(input("Enter a no:"))
b=a*a
print("The sqare of",a, "is",b)
print()
