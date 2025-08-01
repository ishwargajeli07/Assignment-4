#This programme creates a file named output.txt if it doesn't exist already.
#Takes the data to write to file
with open('output.txt' , 'a+' ) as file1:
    data1 = input('Enter text to write to file:')
    file1.write(data1 + '\n')
    print('Data successfully written to output.txt')

#Taking additional data to append
    data2 = input('Enter more data to append to the file:')
    file1.write(data2 + '\n')
    print('Data successfully appended to output.txt')

    print("Final content of output.txt")
    #Moves the cursor to the starting.
    file1.seek(0)
    #Prints the file content
    print(file1.read())
