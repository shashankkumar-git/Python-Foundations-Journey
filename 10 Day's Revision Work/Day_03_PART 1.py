#PROBLEM STATEMENT - Write a for loop that prints numbers from 1 to 20. 
#However, if a number is a multiple of 3, use the continue keyword to skip it so it doesn't print.

for i in range(1,21):
    if i % 3 == 0:
        continue
    else:
        print(f"Number : {i}")