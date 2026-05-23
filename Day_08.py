#PROBLEM STATEMENT - Create a nested dictionary named flight_fleet.
#Add two keys: "Interceptor" and "Bomber".
#Give both of them an inner dictionary containing two keys: "max_speed" (integer) and "stealth_rating" (string: either "High" or "Medium").
#Write an if-else statement that compares their max_speed values and prints out the name of the aircraft that is faster.


flight_fleet = {
    "Interceptor" : {"max_speed" : 2500, "Stealth_rating" : "Medium"} ,

    "Bomber" : {"max_speed" : 4000, "Stealth_rating" : "High"}
}

fastest_speed = 0
fatser_aircraft_name = ""

for aircraft_name , spec in flight_fleet.items():
    if spec["max_speed"] > fastest_speed:
        fastest_speed = spec["max_speed"]
        fatser_aircraft_name = aircraft_name

print(f"The {fatser_aircraft_name} is faster and is flying at the speed of {fastest_speed} km/h")
