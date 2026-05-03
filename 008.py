"""Write a program input a sentence of integers from the keybroad with any length.
The sequence is on one line, and the numbers are separated by spaces.
Calculate the sum of the sequence and display it on the screen."""

valueSequence = input('Enter a sequence of numbers separated by spaces: ')
valueList = valueSequence.split()
print(valueList)
numList = map(int, valueList)
sequenceSum = sum(numList)
print("The sum of the sequence: ", sequenceSum)