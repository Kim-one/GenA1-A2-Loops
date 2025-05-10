# Assignment 2: Explore loops in python

# Task 1: Counting down using loops
# Prompt user for a starting number
starting_num = int(input("Enter starting number: "))

# Loop prints the starting number then continues to decrease until it reaches 1. 
while starting_num>0:
    print(starting_num,end=" ")
    starting_num-=1

print("Blast off! 🚀")

# Task 2:   Multiplication using loops
num = int(input("Enter a number: "))
for i in range(1,11):
    print(f"{num}x{i}=", i*num)

# Task 3: Find the Factorial
# Get user input 
num_fact = int(input("Enter a number: "))

# initialize factorial to 1
fact = 1
# Loop to calculate the factorial. Multiplies each number 'i' by the factorial
for i in range(1, num_fact+1):
    fact*=i

print(f"The factorial of {num_fact} is ", fact)
