#Task 1: You have a list of subjects: subjects = ["Maths", "Physics", "Python", "Chemistry", "Mechanics"]
#Add "Aerospace" to the end of the list.
#Remove "Chemistry".
#Insert "CAD" at the second position (index 1).
#Print the final list and its length.

subjects = ["Maths", "Physics", "Python", "Chemistry", "Mechanics"]
subjects.append("Aerospace")
subjects.remove("Chemistry")
subjects.insert(1,"CAD")
print("Final list - {}, Length of list - {}".format(subjects, len(subjects)))

#############################################################################################################################################

#Task 2: You are given a list of mixed numbers: data = [12, -5, 0, 22, -1, 33, -10, 8]
#Use one line of code (List Comprehension) to create a new list that contains only the positive numbers from the original list

data = [12, -5, 0, 22, -1, 33, -10, 8]
print([x for x in data if x>0])

#############################################################################################################################################

#Task 3: You have a tuple representing a coordinate of your RC plane: coordinate = (23.5, 77.2, 500) representing (latitude, longitude, altitude)
#"Unpack" this tuple into three separate variables named lat, lon, and alt.
#Print a message like: "The plane is at altitude 500m".

coordinate = (23.5, 77.2, 500)
lat, lon, alt = coordinate
print("The plane is at Latitide {}°, Longitude {}° and Altitude {}m".format(lat, lon, alt))

#############################################################################################################################################
 
#Task 4: You have a 3x3 matrix (a list of lists) representing a small grid:
#grid = [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9]
#]
#Print the number 5 by accessing it through the list indices.
#Use a nested for loop to print every number in the grid one by one.

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(grid[1][1])

for row in grid:
    for number in row:
        print(number)
        