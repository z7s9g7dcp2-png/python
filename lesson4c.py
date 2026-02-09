#  A for loop can also be used to iterate through a list , tuple , string or even a dictionary..

name = "Leylahni"

for letter in name:
    print(letter.replace("a", "a -this is letter a"))

for letter in name:
   if letter == "a":
     print("This is letter a")
else:
      print(letter)


print("=============")
#Below is a list of countiess
counties = ["Nairobi","Eldoret","Mombasa","Kisumu","Nakuru","Kajiado","Machakos","Meru", "Embu"]

print(counties)

for county in counties:
    print(county)
    

print("=============")  

for county in counties:
    if county == "Nairobi":
        print("County found")
        break
    else:
        print("County not found")
    
# for county in counties:
#     if "Nairobi" in counties:
#         print("County found")
#     else:
#         print("County not found")


print("=============")  
#The for loop can be ussed to iterate through a dictionary

player = {
    "name":"Mbappe",
    "age": 25,
    "teams":["PSG","Monaco","France"],
    "nationality":"French"
}

for key in player:
    print(key)
    
for values in player:
    print(player[values])


print('=================================')
#loop through the teams the players has played for
for key in player:
    if key == "teams":
        print(player[key])
        
#For team in player["teams"]:
    #print(team)

#print(player["team"])