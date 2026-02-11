#Python Functions
#They are a block of code/statement that performs a given task/action. They can be reused through out the program to perform different tasks.
# Fuctions are defined using the def keyword. (define)
# We have two main types of functions i.e :
# 1. In-Built funtions-> They come preinstalled with the interpreter i.e print(), pop(), range(), appemd() etc....
#2. User defined fuctions -> They are created by a programmer to solve a given task
#To define a function you need to give it a name followec by parenthesis
# For the functions, it is usually indented and to invoke a function we use the function name.


def greetings():
    print("Hello, How are you")

greetings()

print("-------------------------------")
#Addition Function
def addition():
    num1 = 40
    num2 = 50
    sum = num1 + num2
    print("The sum of the numbers is:", sum)

addition()


print("-------------------------------")
#Creae a function that is able to multiply 3 values
def multiplication():
    num1 = 2
    num2 = 3
    num3 = 4
    product = num1 * num2 * num3
    print("The product is", product)

multiplication()

print("-------------------------------") 
#Below is a division function
def divide():
    number1 = int (input("Enter the first number:"))
    number2 = int(input("Enter the second number:"))
    quotient = number1 / number2
    print("The answer is:", quotient) 
    print('----------')
    
for function in range (3):
    divide()