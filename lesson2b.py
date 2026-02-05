#Tuple
#A tuple is an immuta ble type of a list(It cannot change))
#To introduce a tuple we use parenthesis()

counties = ("Nairobi","Mombasa", "Nakuru","Eldoret", "Kajiado","Kisii")
print(counties)
print(type(counties))


#Slicing of tuples
print(counties[3:])

#Accessing Tuples by use of a tuple
print(counties[5])

#Note: Below will generate an error
#Attribute error since tuples are immutable
counties.append("Machakos") 
print(counties)

