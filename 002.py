#Calculate the sum of any two integers (with input exception handling)
#Enter the first value and convert it to an integer
try:
    print('Enter the first number: ')
    num1 = int(input())

#Enter the second value and convert it to an integer
    print('Enter the second number: ')
    num2 = int(input())
    sum = num1 + num2 #Calculate the sum of two numbers

#Display the sum of two numbers on the screen
    print("The sum of two number is: ", sum)    
except:
    print("Invalid input format!")
