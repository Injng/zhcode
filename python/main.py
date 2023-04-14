# main.py
# main functions of zhcode

from os import path
import sys
import stdlib

# dictionary of new functions created by the program
newfunc = {}

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

# translatepy: Given the path of a txt file containing zhPython code, translate it to Python code and write to new file
def translatepy(filename):
    file = path.splitext(filename)[0]  # Get file name without extension
    zh = open(filename, "r")
    py = open(f"{file}.py", "a+")
    lines = zh.readlines()  # Read the file line by line into a list
    state = 0  # Use a state variable to preserve continuity
    bstate = 0  # Use a specialized state variable for brackets
    sstate = 0  # Use a specialized state variable for strings
    linenum = 0  # Count line numbers
    for x in lines:  # Iterate over the list to translate
        linenum += 1
        length = len(x)
        # Get list of keys for translation dictionaries
        name_keys = list(stdlib.names.keys())
        func_keys = list(stdlib.func.keys())
        newfunc_keys = list(newfunc.keys())
        dunder_keys = list(stdlib.dunder.keys())
        for i in range(length):
            if state == 0 or state == 1:
                # Check if character is within any of the keys of translation dictionaries
                innames = inkey(x[i], name_keys)
                infunc = inkey(x[i], func_keys)
                innewfunc = inkey(x[i], newfunc_keys)
                indunder = inkey(x[i], dunder_keys)
                # Check for strings
                if x[i] == '"':
                    if sstate == 1:  # State to ignore strings
                        py.write('"')
                        sstate = 2
                    elif sstate == 2:  # State to end the ignoring period
                        py.write('"')
                        sstate = 0
                    else:
                        try:
                            if x[i + 1] == "—" and x[i + 2] == "—" and x[i + 4] == "—" and x[i + 5] == "—":  # Check for __main__
                                if x[i + 3] == "主":
                                    py.write('"__main__"')
                                    state = -6
                                else:
                                    py.write('"')
                                    state = 4
                            else:
                                py.write('"')
                                state = 4
                        except:
                            py.write('"')
                            state = 4
                elif x[i] == "'":
                    if state == 1:  # State to ignore strings
                        py.write("'")
                        state = 2
                    elif state == 2:  # State to end the ignoring period
                        py.write("'")
                        state = 0
                    else:
                        try:
                            if x[i + 1] == "——" and x[i + 3] == "——":  # Check for __main__
                                if x[i + 2] == "主":
                                    py.write("'__main__'")
                                    state = -4
                                else:
                                    py.write("'")
                                    state = 4
                            else:
                                py.write("'")
                                state = 4
                        except:
                            py.write("'")
                            state = 4
                # Check for dunder methods
                elif x[i] == "—":
                    if indunder != -1:
                        dunderkey = dunder_keys[indunder]
                        matchindex = matchkey(x, i, dunderkey)
                        if matchindex != 0:
                            py.write(stdlib.dunder.get(dunderkey))
                            state = -1 * (matchindex - 1)
                        else:
                            errprint(filename, linenum, x)
                            print("TranslateError: dunder method not found")
                            sys.exit()
                    else:
                        errprint(filename, linenum, x)
                        print("TranslateError: dunder method not found")
                        sys.exit()
                # Check for names
                elif innames != -1:
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
                        if stdlib.func.get(funckey) == "format":  # Check for string format exception
                            if state == 1:
                                pass
                            elif x[i + 2] == '"' or x[i + 2] == "'":
                                py.write("f")
                                sstate = 1
                            else:
                                pass
                        else:
                            py.write(stdlib.func.get(funckey))
                            state = -1 * (matchindex - 1)
                # Check for program-created functions
                elif innewfunc != -1:
                    newfunckey = newfunc_keys[innewfunc]
                    matchindex = matchkey(x, i, newfunckey)
                    if matchindex != 0:
                        py.write(newfunc.get(newfunckey))
                        state = -1 * (matchindex - 1)
                # Check for keywords
                elif x[i] in stdlib.keywords:
                    py.write(stdlib.keywords.get(x[i]) + " ")
                    if stdlib.keywords.get(x[i]) == "def":
                        state = 3
                # Check for variable delimiter
                elif x[i] == "「":
                    index = 0
                    for j in range(i + 1, length):
                        index += 1
                        if x[j] == "」":
                            py.write(" ")
                            break
                        else:
                            py.write(x[j])
                    state = -1 * index
                # Check for central dot punctuation
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
                # Check for bracket notation
                elif x[i] == "【":
                    py.write("[")
                elif x[i] == "】":
                    py.write("]")
                # Check for carats
                elif x[i] == "《":
                    py.write("<")
                elif x[i] == "》":
                    py.write(">")
                # Check for period punctuation
                elif x[i] == "。":
                    if bstate == 1:
                        py.write("}")
                        bstate = 0
                    else:
                        py.write("{")
                        bstate = 1
                # Otherwise, must be the same
                else:
                    py.write(x[i])
            elif state < 0:  # State used for ignoring
                state = state + 1
            elif state == 3:  # State used for determining name of new function
                funcname = ""
                index = 0
                for j in range(i, length):
                    if x[j] == "（":
                        break
                    else:
                        index += 1
                        funcname += x[j]
                newfunc[funcname] = funcname
                py.write(funcname)
                state = -1 * (index - 1)
            elif state == 4:  # State used for copying contents of a string
                if x[i] == '"' or x[i] == "'":
                    py.write(x[i])
                    state = 0
                else:
                    py.write(x[i])
            else:
                pass

translatepy("test.txt")
