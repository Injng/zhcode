# helper.py
# helper functions for translate

# determine if string is in any part of a dictionary key and if so return the index of the key, otherwise return -1
def inkey(x, keys):
    length = len(keys)
    for k in range(length):
        if x in keys[k]:
            return k
        else:
            pass
    return -1

# find if entire string matches the key and if so return the length of the key, otherwise return 0
def matchkey(x, i, key):
    length = len(key)
    if length == 1:
        return 1
    else:
        for j in range(length):
            try:
                if x[i + j] == key[j]:
                    pass
                else:
                    return 0
            except:
                return 0
        return length

# General print of filename and line for error handling
def errprint(name, line, x):
    print(f"File {name}, line {line}")
    print(f"    {x}")
