#name rearrangement

import re
'''
def name_rearrange(name):
    result = re.search(r'(\w*), (\w*)$', name.title())
    if result == None:
        return name
    return '{} {}'.format(result[2], result[1])

print(name_rearrange("sajan, sarker"))
'''

def name_rearrange(name):
    result = re.search(r'^(\w*), ([\w .-]*)$', name.title())
    if result == None:
        return name
    return '{} {}'.format(result[2], result[1])

print(name_rearrange("sarker, sajan k."))