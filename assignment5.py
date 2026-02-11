# Function Without parameters
# Create a function that takes no parameters , uses arithmetic operation to calculate area of rectangle and print the results
def rectangle_area():
    length = 10
    width = 5
    area = length * width
    print(f"The area of the rectangle is: {area}")
rectangle_area()

#Function with parameters
# Create a function that accepts parameters returns their sum, difference, product and division

def operations(num1, num2):
    addition = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    
    if num2 != 0:
        division = num1 / num2
    else:
        division = "Undefined (cannot divide by zero)"
        
    
    return addition, difference, product, division
sum, diff, prod, div = operations(10, 2)
print(f"Sum: {sum}, Difference: {diff}, Product: {prod}, Division: {div}")


#Control Statements(if.....elif...else)
#write a function that accepts a number that checks whether the number is positive negative or zero

def check_number():
    
    user_input = input("Enter a number to check: ")
    
    number = float(user_input)
    
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("The number is Zero")

check_number()

#Loop with arithmetic
#A function that accepts a number n uses a for loop and calculates the sum of numbers from 1 to n

def calculate_sum(n):
    total_sum = 0
    
    for i in range(1, n + 1):
        total_sum += i
        
    return total_sum

result = calculate_sum(5)
print(f"The sum of numbers from 1 to 5 is: {result}")


# While loop
# Write a function that accepts a number uses a while loop and calculates the squares of numbers from 1 upto that number
def squares():
    
    user_input = input("Enter a number: ")
    
    try:
        n = int(user_input)
        count = 1
        
        while count <= n:
            square = count * count
            print(f"The square of {count} is {square}")
            
            count += 1
            
    except ValueError:
        print("Please enter a valid whole number.")

squares()
