#PROBLEM STATMENT - You receive a raw flight coordinate log string: log = "LAT:23.55_LON:77.21_ALT:1200". 
# Write a function called parse_coordinates(log_string) that splits this text by the underscore character (_) and prints 
# each metric on a clean, separate line using an f-string


log = "LAT:23.55_LON:77.21_ALT:1200"

def parse_coordinates(log_string):
    list = log_string.split("_")

    for item in list:
        identifier , value = item.split(":")        ##Think this as -->  x , y = 10 , 20

        print(f"{identifier} ---> {value}")
    
parse_coordinates(log)    