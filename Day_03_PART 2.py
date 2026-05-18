#Task 1: Write a program that calculates the sum of all even numbers from 1 to 50.
#        Hint: Use range(2, 51, 2) or an if statement with the modulo % operator.

sum = 0
for i in range(1,51):
    if i % 2 == 0:
        sum += i
    else:
        continue
print("Sum of even no's upto 50 is:",sum)

#############################################################################################################################################

#Task 2: Use a while loop to create a simple password checker.
#        Define a variable correct_password = "Python123".
#        Keep asking the user to "Enter Password" until they get it right.
#        Once they get it right, print "Access Granted."


correct_password = "Python123"
password = input("Enter the Password:")

while password != correct_password:
    print("Your entered password is in correct.\nPlease enter the password again\n")
    password = input("Wrong. Try again:")

    if password == correct_password:
        print("Access Granted")

#############################################################################################################################################

#Task 3: Use nested for loops to print a right-angled triangle of stars (*). It should look like this:
#     *
#     **
#     ***
#     ****
#     *****
#     Hint: The outer loop handles the rows, and the inner loop handles how many stars are in that row.


for i in range(11):
    for x in range(i+1):
        a = "*"    
    print(a*x)

#############################################################################################################################################

#Task 4: Write a program to check if a number entered by the user is a Prime Number.
#      Logic: A prime number is only divisible by 1 and itself.
#      Hint: Use a for loop to try dividing the user's number by every number from 2 up to the
#      square root of that number (or just half of it). If any division results in a remainder of 0, it’s
#      not prime. Use the break keyword as soon as you find a divisor!


n = int(input("Enter the Number: "))

for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        print("The number", n, "is not a prime number")
        break
else:
    print(n, "is a Prime Number")
