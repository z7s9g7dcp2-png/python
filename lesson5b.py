#Functions with parameters
#Parameters- they are values that get passed as arguments given to a function inside of the parenthesis

def greeting (name):
    print(f"{name} How are you? Hope everything is fine")

greeting("Leylahni")
greeting("yasmin")

print('---------------------------')
def message (names):
    print(f"Hello,{names}.We shall be having a meeting on date........Please avail yourself")

message("Shurabi")

# print('---------------------------')
# for x in range (1000):
#     message()
#     print(x)


print('---------------------------')
#Craete a function that accepts parameters to add two numbers
def sum(x, y):
    addition= x + y
    print(f"The sum of the numbers is, {addition}")
sum( 5 , 10)