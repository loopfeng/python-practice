#04 Enter any decimal number and display it in octal 

#Self-written code
a = float(input())
b = float(a/8)
print("Decimal number", float(a), "it octal is ", float(b))

#Sample code 
#Input a value from the keyboard and convert it to integer 
decimal = int(input())

# Out the sentence in the required fromat
# %d is used to hold a decimal integer value 
# %o is used to hold an octal value 
print('Decimal number %d in octal is %o' % (decimal, decimal))

#Redo
decimal = int(input())
print("Decimal number %d in octal is %o ----- %o" % (decimal, decimal))

#Redo (Recommended)
num = int(input())
print(f"Decimal number {num} in octal is {oct(num)[2:]}")# f = short for "formatted string"