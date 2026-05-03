"""Input and calculate the sum of any sequence of integers 
separated by spaces (with input exception handling)."""

valueSequence = input('Enter a sequence of numbers saparated by spaces: ')
valueList = valueSequence.split()
try:
    if valueSequence == "#nothing":
        print(0)
    else:
        numList = map(int, valueList)
        sequenceSum = sum(numList)
        print("The sum of the sequence: ", sequenceSum)
except:
    print('Invalit input format!')