import re
result = re.search(r'^(\w*), (\w*)$',"Ada, Lovelace")
print(result)
print(result.groups())
print(result[0])
print(result[1])
print(result[2])
print("{} {}".format(result[1], result[2]))