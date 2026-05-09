"""Read input from a file {name}, {current age}, and write the output
to a file according to the sample output."""

# Practice version
with open('input.inp', 'r') as inputFile:
    name = inputFile.readline().rstrip('\n')
    currentAge = int(inputFile.readline().rstrip('\n'))

with open('output.out', 'w') as outputFile:
    outputFile.write(
        'In 20 years, {} will be {}'.format(name, currentAge + 20)
    )


# Sample version
# Open the file with mode='r' to read the file
with open('input.inp', 'r') as inputFile:

   # Read one line from the file and store it in variable name
   # Use the rstrip method to remove the newline character '\n'
   name = inputFile.readline().rstrip('\n')

   # Read one line from the file and store it in variable currentAge
   currentAge = int(inputFile.readline())

# Open the file with mode='w' to write to the file
with open('output.out', 'w') as outputFile:

   # Write content to the file according to the sample format
   outputFile.write(
       'In 20 years, {} will be {}'.format(name, currentAge + 20)
   )