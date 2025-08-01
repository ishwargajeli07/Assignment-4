# This program reads a file and shows its content
try:
    # Try to open the file named 'sample.txt' in read mode
    with open('sample.txt', 'r') as file1:
        print("Reading file content:")

        # Read the first line and print it
        print('Line 1:', file1.readline())

        # Read the second line and print it
        print('Line 2:', file1.readline())

except FileNotFoundError:
    # If the file does not exist, print this message
    print('File not found')

# This will always be printed.
print("Thank You.")
