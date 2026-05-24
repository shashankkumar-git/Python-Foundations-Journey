#PROBLEM STATEMENT -You are given a raw list of data packets coming from a tracking system. Some packets are corrupt ("DROP"), while 
# valid packets contain an aircraft ID, airspeed (knots), and altitude (feet) mashed into a single string.
# # The Core Challenges Your Code Must Solve:
# 1]The Cleaning Layer: Loop through radar_stream. If a packet doesn't contain a colon (":"), it is corrupt. 
# Use the continue keyword to skip it immediately.

# 2]The Double-Split Unpacking Layer: For valid packets, use your .split(":") mechanism to separate the aircraft name from its telemetry.
#  Then, split again to isolate the numerical values from SPD= and ALT=. Convert those final values to integers.

# 3]The Dynamic Dictionary Aggregator: You need to build a master telemetry tracker called fleet_summary. The catch? You cannot hardcode 
# the aircraft names. Your code must detect them on the fly.

# Logic Flow: As the loop runs, check if the aircraft is already a key in your dictionary. If it isn't, add it with a nested layout 
# holding empty lists: {"speeds": [], "altitudes": []}. Then, append the values to those lists!

# 4]The Engineering Metrics Dashboard: After processing the stream, use a for loop with .items() to loop through your final fleet_summary 
# dictionary. For each aircraft, use sum() and len() to calculate its average airspeed and maximum altitude, and print it dynamically using 
# f-strings with a sleek terminal separator line (---).

#When your script finishes running in your terminal, it should output a clean dashboard matrix without you ever typing a specific 
# aircraft name in a print statement:


#  =================== FLEET TELEMETRY REPORT ===================
#Aircraft: FIGHTER_A
# -> Avg Airspeed: 457.5 knots
# -> Max Altitude: 12500 feet
#--------------------------------------------------------------
#Aircraft: FIGHTER_B
# -> Avg Airspeed: 600.0 knots
# -> Max Altitude: 18000 feet
#--------------------------------------------------------------
#Aircraft: FIGHTER_C
# -> Avg Airspeed: 1200.0 knots
# -> Max Altitude: 35000 feet
#==============================================================

radar_stream = [
    "FIGHTER_A:SPD=450:ALT=12000",
    "FIGHTER_B:SPD=610:ALT=18000",
    "CORRUPT_DATA_DROP_PACKET",
    "FIGHTER_A:SPD=465:ALT=12500",
    "FIGHTER_B:SPD=590:ALT=17500",
    "FIGHTER_C:SPD=1200:ALT=35000"
]

fleet = {}
def fleet_summary(data_packets):
    for packets in data_packets:
        if ":" not in packets:
            continue

        list_1 = packets.split(":")
        aircraft_name = list_1[0]
        
        _, speed = list_1[1].split("=")             # other way of writing this is [ int(list_1[1].split("=")[1]) ]
        speed = int(speed)
        
        _, altitude = list_1[2].split("=")
        altitude = int(altitude)                                      # [ int(list_1[2].split("=")[1]) ]

        if aircraft_name not in fleet:
            fleet[aircraft_name] = {"speeds" : [], "altitude" : []}
        
        fleet[aircraft_name]["speeds"].append(speed)
        fleet[aircraft_name]["altitude"].append(altitude)

    print("="*10, " FLEET TELEMETRY REPORT ", "="*10)

    for name, data in fleet.items():
        
        avg_speed = sum(data["speeds"]) / len(data["speeds"])
        max_altitude = max(data["altitude"])

        print(f"Aircraft: {name}")
        print(f"--> Avg Airspeed: {avg_speed:.1f} knots")
        print(f"--> Max Altitude: {max_altitude} feet")
        print("-" * 62)


fleet_summary(radar_stream)
