#A dictionary is a data type that stores data in terms of key- value pair
# It is introduced by the use of curly braces {}
# The values stored inside of a dictionary can be of any data type. 
#To access the values in a dictionary we use the keys


phonebook = {
    "Benson" : "12345678",
    "Mary" : "90123457",
    "Stephen" : "2345789"
}

#Showing the entire dictionary
print(phonebook)
print(type(phonebook))

#Printing out Bensons number
print(phonebook["Benson"])


print('==================')


players = {
    "Name" : "Messi",
    "Age" : 40,
    "Teams" :["PSG", "Barcelona","Argentina"]
}

#print Barcelona
print(players["Teams"][1])