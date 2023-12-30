import re

result = (re.search(r'aza', 'plaza')) 
print(result)
# <re.Match object; span=(2, 5), match='aza'>

print(re.search(r'aza', 'bazaar')) 
# <re.Match object; span=(1, 4), match='aza'>

print(re.search(r'aza', 'maze'))
# None  

print(re.search(r'^x', 'xenon'))
# <re.Match object; span=(0, 1), match='x'>

print(re.search(r'p.ng', 'penguin'))
# <re.Match object; span=(0, 4), match='peng'>

print(re.search(r'p.ng', 'clapping'))
# <re.Match object; span=(4, 8), match='ping'>

print(re.search(r"[Pp]ython", "Python"))
# <re.Match object; span=(0, 6), match='Python'>

print(re.search(r"[a-z]way", "The end of the highway"))
# <re.Match object; span=(18, 22), match='hway'>

print(re.search(r"[a-z]way", "What a way to go"))
# None

print(re.search("cloud[a-zA-Z0-9]", "cloudy"))
# <re.Match object; span=(0, 6), match='cloudy'>

print(re.search("cloud[a-zA-Z0-9]", "cloud9"))
# <re.Match object; span=(0, 6), match='cloud9'>

print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
# <re.Match object; span=(4, 5), match=' '>

print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))
# <re.Match object; span=(30, 31), match='.'>

print(re.search(r"cat|dog", "I like cats."))
# <re.Match object; span=(7, 10), match='cat'>

print(re.search(r"cat|dog", "I love dogs!"))
# <re.Match object; span=(7, 10), match='dog'>

print(re.search(r"cat|dog", "I like both dogs and cats."))
# <re.Match object; span=(12, 15), match='dog'>

print(re.findall(r"cat|dog", "I like both dogs and cats."))
# ['dog', 'cat']

print(re.search(r"Py.*n", "Pygmalion"))
# <re.Match object; span=(0, 9), match='Pygmalion'>

print(re.search(r"Py.*n", "Python Programming"))
# <re.Match object; span=(0, 17), match='Python Programmin'>

print(re.search(r"Py[a-z]*n", "Python Programming"))
# <re.Match object; span=(0, 6), match='Python'>

print(re.search(r"Py[a-z]*n", "Pyn"))
# <re.Match object; span=(0, 3), match='Pyn'>

print(re.search(r"o+l+", "goldfish"))
# <re.Match object; span=(1, 3), match='ol'>

print(re.search(r"o+l+", "woolly"))
# <re.Match object; span=(1, 5), match='ooll'>

print(re.search(r"o+l+", "boil"))
# None

print(re.search(r"p?each", "To each their own"))
# <re.Match object; span=(3, 7), match='each'>

print(re.search(r"p?each", "I like peaches"))
# <re.Match object; span=(7, 12), match='peach'>

print(re.search(r".com", "welcome"))
# <re.Match object; span=(2, 6), match='lcom'>

print(re.search(r"\.com", "welcome"))
# None

print(re.search(r"\.com", "mydomain.com"))
# <re.Match object; span=(8, 12), match='.com'>

print(re.search(r"\w*", "This is an example"))
# <re.Match object; span=(0, 4), match='This'>

print(re.search(r"\w*", "And_this_is_another"))
# <re.Match object; span=(0, 20), match='And_this_is_another'>

print(re.search(r"\d", "015"))
# <re.Match object; span=(0, 1), match='0'>

print(re.search(r"\d*", "123456789"))
# <re.Match object; span=(0, 9), match='123456789'>

print(re.search(r"A.*a", "Argentina"))
# <re.Match object; span=(0, 9), match='Argentina'>

print(re.search(r"A.*a", "Azerbaijan"))
# <re.Match object; span=(0, 9), match='Azerbaija'>

print(re.search(r"^A.*a$", "Australia"))
# <re.Match object; span=(0, 9), match='Australia'>

pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid_variable_name"))
# <re.Match object; span=(0, 30), match='_this_is_a_valid_variable_name'>

print(re.search(pattern, "this isn't a valid variable"))
# None

print(re.search(pattern, "my_variable1"))
# <re.Match object; span=(0, 12), match='my_variable1'>

print(re.search(pattern, "2my_variable1"))
# None