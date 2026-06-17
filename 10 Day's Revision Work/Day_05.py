#PROBLEM STATEMENT - Create a dictionary student with name, roll_no, and marks (as a list: [80, 90, 85])
#Add a new key college with the value "VIT Bhopal".
#Calculate the average of the marks list inside the dictionary and print it.

details = {
    "Name" : "Shashank",
    "Roll_No" : "12345",
    "Marks" : [80, 90, 85]
}

details["College"] = "VIT Bhopal"
print(details)

total_marks = sum(details["Marks"])

average_marks = total_marks / len(details["Marks"])

print(f"Average Marks - {average_marks:.2f}")