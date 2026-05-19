#PROBLEM STATEMENT - You have a list of sensor readings from a prototype aircraft: readings = [10.2, 15.5, 9.8, 20.1, 12.3, 25.4].
#                    Use a List Comprehension to create a new list called high_readings that only contains values greater than 15.0


readings = [10.2, 15.5, 9.8, 20.1, 12.3, 25.4]

high_readings = [x for x in readings if x>15.0]
print(high_readings)