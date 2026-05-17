#PROBLEM STATEMENT - Create a "Flight Eligibility" checker. A user needs to be over 18 AND have a valid ID (a boolean variable) to pass.
age = int(input("Enter Your AGE: "))

Having_Valid_id = input("Do you have a valid ID? (True/False): ")

if age < 18:
    print("You are under age and not elgibile to travel in the flight")

else:
    if Having_Valid_id == "False":
        print("Not elgible for this Flight due to invalid id")

    else:
        print("You are eligible for the flight")
        print("Wishing you a safe and peaceful journey")