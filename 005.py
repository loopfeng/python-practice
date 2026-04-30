# 05 Enter any decimal number and display it in octal(with input exception handling)
value = input()

# isParseDone = a variable used to check whether data processing (parsing) is done or not.
isParseDone = False
try:
    decimal = int(value)
    isParseDone = True
except:
    print("Invalit input format!")

if isParseDone:
    print("Decimal %d in octal is %o" % (decimal, decimal))
