# Python Lists
# A list in python is a collection of items thats ordered in a certain way.
#Lists in python are introduces by the use of the square brackets []
#The items of a alist are stored inside of indexes. Note:In programming we start counting from index Zero(0)
#A list is mutable i.e its contents can be changes

cars = ["BMW", "Benze", "Hiance","Prado", "Probox", "Mclaren", "Range"]

print(cars)
print(type(cars))

#Accessing items of a list
print(cars[2])
print("The car on index four is:", cars[4])


#List slicing - This is creating a list from a given bigger list
print(cars[4:])


#Printing from index 0 to 3
print(cars[:4])

#Printing from hiance to probox
print(cars[2:5])


#List - Mutability
#we use the function append to add an item at the end of a list
cars.append("Mercedes")
print(cars)

cars.append("Subaru")
print(cars)


#We use the pop function to remove an item at the end of the list
cars.pop()
print(cars)

#we can use an index to add items to a list
cars[5] = "Pajero"
print(cars)

#We can use the sort function to sort out items in alphabetical order
cars.sort()
print(cars)

del cars[4]
print(cars)

cars.pop(4)
print (cars)

cars.remove("BMW")
print(cars) 