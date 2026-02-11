# number = 100 / 0
# print(number)

# Onthe try and except block: You run some codes/statements and if it is succesful the try block will get executed other the except block will be executed wthen there is an anticipated error


try:
    number = 100
    answer = number / 10
    print("The answer is:", answer)
except Exception as e:
    print("There is an error:", e)