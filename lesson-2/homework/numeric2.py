
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))

# Find the largest and smallest numbers
largest = max(number1, number2, number3)
smallest = min(number1, number2, number3)

# Output the results
print("The largest number is: " + str(largest))
print("The smallest number is: " + str(smallest))