# main.py
# main functions of zhcode

from os import path
import sys
import stdlib

# list of new functions created by the program
newfunc = []

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

# translatepy: Given the path of a txt file containing zhPython code, translate it to Python code and write to new file
def translatepy(filename):
    file = path.splitext(filename)[0]  # Get file name without extension
    zh = open(filename, "r")
    py = open(f"{file}.py", "a+")
    lines = zh.readlines()  # Read the file line by line into a list
    state = 0  # Use a state variable to preserve continuity
    for x in lines:  # Iterate over the list to translate
        length = len(x)
        name_keys = list(stdlib.names.keys())
        func_keys = list(stdlib.func.keys())
        for i in range(length):
            if state == 0:
                innames = inkey(x[i], name_keys)
                infunc = inkey(x[i], func_keys)
                # Check for names
                if innames != -1:
                    nameskey = name_keys[innames]
                    matchindex = matchkey(x, i, nameskey)
                    if matchindex != 0:
                        py.write(stdlib.names.get(nameskey))
                        state = -1 * (matchindex - 1)
                # Check for functions
                elif infunc != -1:
                    funckey = func_keys[infunc]
                    matchindex = matchkey(x, i, funckey)
                    if matchindex != 0:
                        py.write(stdlib.func.get(funckey))
                        state = -1 * (matchindex - 1)
                # Check for keywords
                elif x[i] in stdlib.keywords:
                    py.write(stdlib.keywords.get(x[i]) + " ")
                    if stdlib.keywords.get(x[i]) == "def":
                        state = 2
                # Check for variable delimiter
                elif x[i] == "【":
                    index = 0
                    for j in range(i + 1, length):
                        index += 1
                        if x[j] == "】":
                            break
                        else:
                            py.write(x[j])
                    state = -1 * index
                # Check for period punctuation
                elif x[i] == "·":
                    py.write(".")
                # Check for parantheticals
                elif x[i] == "（":
                    py.write("(")
                elif x[i] == "）":
                    py.write(")")
                # Check for colon
                elif x[i] == "：":
                    py.write(":")
                # Check for comma
                elif x[i] == "，":
                    py.write(",")
                # Otherwise, must be the same
                else:
                    py.write(x[i])
            elif state < 0:  # State used for ignoring
                state = state + 1
            elif state == 2:  # State used for determining name of new function
                funcname = ""
                index = 0
                for j in range(i, length):
                    if x[j] == "（":
                        break
                    else:
                        index += 1
                        funcname += x[j]
                newfunc.append(funcname)
                py.write(funcname)
                state = -1 * (index - 1)
            else:
                pass
