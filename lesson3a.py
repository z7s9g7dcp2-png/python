#Boolen- this is a data type that evaluates either to true or false

isRaining = False
print(isRaining)
print(type(isRaining))

paidLoan = True
print(paidLoan)
print(type(paidLoan))


#comparison operators: They are useed to compare two or more statements and they are usually return a boolean answer

number1 = 2
number2 = 5

print("is number1 greater than number2?", number1 > number2)
print("is number1 less than number2?", number1 < number2)

print("is number1 greater than or equal to number2?", number1 >= number2)
print("is number1 less than or equal to number2?", number1 <= number2)

print("is number1 equal to number2?", number1 == number2)
print("is number1 not equal to number2?", number1 != number2)

#logical operators
#Logical and
#it returns true only one of the condition/statements evaluates true
print((3 > 1) and (7 > 6))

#logical or
# It evaluates to true if one of the statements/conditions is true
print((3 > 1) or (7 < 6))

#logical not
#It is used to negate a statement/a condition
print(not(90 > 70))
