"""06 Write a program to round the decimal number A to B digits after the decimal point.
A and B are entered from the keyboard. Display the rounded value of A on the screen."""
a = float(input("Enter the decimal number A: "))
b = int(input("Enter an integer B: "))
# Format 
print('Format used: {0:.{1}f}'.format(a,b))
#Use the rould() function
formatedNum = round(a, b)
print('rould used', formatedNum)