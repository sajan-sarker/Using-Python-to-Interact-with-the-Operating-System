# in terminal type: python3 
# if we open a file with open function, we have to close it with close function
file = open("song.txt", "r")
# read one line from the file
print(file.readline())
# read the whole file 
print(file.read())

file.close()


print()
print()
# another way to open a file is with the with statement
# with statement will automatically close the file for us

with open("song.txt", "r") as file:
    print(file.read())

