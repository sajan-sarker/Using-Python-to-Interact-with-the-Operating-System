import re

def rearrange_name(name):
    result = re.search(r'^([\w .]*), ([\w .]*)$', name)
    if result == None:
        return name
    return '{} {}'.format(result[2], result[1])

#name = input("Enter name (last name, first name): ")
#print(rearrange_name(name))

