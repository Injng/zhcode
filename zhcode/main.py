# main.py
# main functions of zhcode

from os import path, remove
from sys import exit
import zhcode.python.translate


# Function to translate text file
def zhtrans(file, lang, mode='k'):
    if lang == "py":
        zhcode.python.translate.translatepy(file)
        if mode == 'd':
            remove(file)
    else:
        print(f"TranslateError: language not supported: {file}")
        exit()

# Function to translate and execute file
def zhexec(file, lang, mode='k'):
    if lang == "py":
        zhcode.python.translate.translatepy(file)
        if mode == 'd':
            remove(file)
        filename = path.splitext(file)[0] + '.py'
        try:
            return exec(open(filename).read())
        except:
            print(f"TranslateError: no such file or directory: {filename}")
            exit()
    else:
        print(f"TranslateError: language not supported: {file}")
        exit()

# Function to translate multi-line string
def zhtrstr(code, lang, name='test.txt'):
    with open(name, "w+") as f:
        try:
            f.writelines(code)
        except:
            print("TranslateError: input string formatted incorrectly")
            exit()
    zhtrans(name, lang, 'd')

# Function to translate and execute multi-line string
def zhexstr(code, lang, name='test.txt'):
    with open(name, "w+") as f:
        try:
            f.writelines(code)
        except:
            print("TranslateError: input string formatted incorrectly")
            exit()
    return zhexec(name, lang, mode='d')

