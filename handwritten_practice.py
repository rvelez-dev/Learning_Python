# create a program to read someone's name
'''
name = input("Enter your name ")
print(name)
'''


#create a program to take in two numbers add them, subtract them, and multiply them
'''
num_1 = int(input("Enter first number "))
num_2 = int(input("Enter second number "))
add = num_1 + num_2
subtract = num_1 - num_2
multiply = num_1 * num_2
print(add)
print(subtract)
print(multiply)
'''


#create a program to take in two words and make them into one word
'''
word_1 = input("Enter Word ")
word_2 = input("Enter Word ")
together = word_1 +" "+word_2
print(together)
'''

#given a list of numbers 1-5 calculate the sum
"""
list=[1,2,3,4,5]
sum = 0
for n in list:
    sum = sum + n
print(sum)
"""

#create a program that checks if a users num is even or odd
'''
num = int(input("Enter number "))
if num % 2 ==0:
    print("Your number is even")
else:
    print("Your number is odd")
'''

#create a program to receive a users test score and give user A,B,C, or D depending on grade

grade = int(input("Enter your grade "))
if grade >= 90:
    print("You got an A ")
elif grade >=80 and grade <90:
    print("You got a B ")
elif grade >=70 and grade <80:
    print("You got a C ")
elif grade >=60 and grade <70:
    print("You got a D ")
else:
    print("You failed")



