# in terminal
with open ("novel.txt", "w") as file:
    file.write("It was a dark and stormy night")

with open ("novel.txt", "r") as file:
    print(file.read())