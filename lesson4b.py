# Loops ->someties we may need to do a piece of work a number of repeated times in such cases we may use loops
# A loop is a control structure that allows us to execute a certain condition is met
# There are two types of loops in python

# Below is the syntax of a for loop in python
"""
for variable in range(n):
    #block of code to be executed
"""
#print("Hello Yasmin")
#print("Hello Yasmin")
#print("Hello Yasmin")
#print("Hello Yasmin")

for greeting in range(4):
    print("Hello Yasmin", greeting)

print('==========================')

for number in range(10,20):
    print(number)

print('==========================')
#Find the even number in the range of 50 to 71
for number in range (50,71,2):
    print(number)  



print('==========================')
#Create a python program that prints the odd numbers from 100 to 150
for number in range (101,150,2):
        print(number)


print('==========================')
#create a program that prints the multiples of 3 starting from 201 to 150
for number in range(201, 149, -3):
    print(number)

print('==========================')
#Create a python program that prints the leap years in beteween 2000 to 2024
for year in range(2000, 2025, 4):
    print(year)