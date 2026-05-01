"""write a program to round the decimal number A to B digits after the decimal point.
A and B are entered from the keyboard. Display the rounded value of A on the screen
(with input exception handling)"""
valueA = input()
valueB = input()

isParseDone = False
try:
    numA = float(valueA)
    numB = int(valueB)
    isParseDone = True
except:
    print('Invalit input format!')

if isParseDone:
    # Format 
    print('Dùng format: {0:.{1}f}'.format(numA, numB))
    #Use the round() function
    formatedNum = round(numA, numB)
    print('round used', formatedNum)