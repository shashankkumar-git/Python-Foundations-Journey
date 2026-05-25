#PROBLEM STATMENT - You will build a system where the safety rules are separate, independent functions, and a master controller 
# dynamically evaluates them.
# # 1] Write the Independent Rule Functions
# Write two clean, separate functions that return True if there is a danger, and False if it's safe:
# check_overspeed(data): Returns True if data["speed"] > 1000.
# check_overheat(data): Returns True if data["temp"] > 200 

# 2] Instead of writing if check_overspeed() or check_overheat(): inside your loop, you are going to map these functions directly 
# inside a tracking dictionary. In Python, functions are objects, meaning you can store a function name inside a dictionary without
#  the parenthesis!

# # Mapping the rule functions dynamically
# safety_rules = {
#     "CRITICAL OVERSPEED": check_overspeed,
#     "CRITICAL OVERHEAT": check_overheat
# }

# # 3] The Evaluation Pipeline
# Now, write your master execution loop.
# Loop through telemetry_log.items() to get each aircraft_id and its specs dictionary.
# Inside that loop, write a nested loop that iterates through your safety_rules.items() dictionary to get the alert_name and the rule_function.
# Execute the function dynamically on the fly by passing the aircraft specs to it:
# # This runs the mapped function dynamically!
# if rule_function(specs) == True:
#     print(f"[ALERT] {aircraft_id} Triggered {alert_name}!")

# When you run your final script in VS Code, it should output exactly like this:
# =================== SYSTEM SAFETY MONITOR ===================
# [ALERT] AC_02 triggered CRITICAL OVERSPEED! (Value: 1200)
# [ALERT] AC_03 triggered CRITICAL OVERHEAT!  (Value: 245)
# [ALERT] AC_04 triggered CRITICAL OVERSPEED! (Value: 1100)
# [ALERT] AC_04 triggered CRITICAL OVERHEAT!  (Value: 220)
# [ALERT] AC_07 triggered CRITICAL OVERSPEED! (Value: 1350)
# =============================================================





telemetry_log = {
    "AC_01": {"speed": 450, "altitude": 12000, "temp": 145},   # Healthy
    "AC_02": {"speed": 1200, "altitude": 35000, "temp": 180},  # Overspeeding
    "AC_03": {"speed": 400, "altitude": 8000, "temp": 245},    # Overheating
    "AC_04": {"speed": 1100, "altitude": 42000, "temp": 220},  # Both!
    "AC_05": {"speed": 550, "altitude": 15000, "temp": 150},   # Healthy
    "AC_06": {"speed": 480, "altitude": 11500, "temp": 142},   # Healthy
    "AC_07": {"speed": 1350, "altitude": 29000, "temp": 195}   # Overspeeding
}


def check_overspeed(data):
    if data["speed"] > 1000:
        return data["speed"]
    return False

def check_overheat(data):
    if data["temp"] > 200:
        return data["temp"]
    return False

safety_rules = {
    "CRITICAL OVERSPEED": check_overspeed,
    "CRITICAL OVERHEAT": check_overheat
}

datas = {}
def check_details(log_report):
    print("="*10, "SYSTEM SAFETY MONITOR", "="*10)

    for AC_name, specs in log_report.items():
        aircraft_name = AC_name

        for alert_name , rule_function in safety_rules.items():

            result = rule_function(specs)

            if result != False:
                print(f"[ALERT] {aircraft_name} triggered {alert_name}! (Value: {result})")

check_details(telemetry_log)