# in terminal type: python3
# open file with with statement
with open("song.txt", "r") as file:
    for line in file:
        print(line.upper().strip())

print()
print()
# another format
file = open("song.txt", "r")
lines = file.readlines()
file.close()
lines.sort()
print(lines)

for line in lines:
    print(line.strip())