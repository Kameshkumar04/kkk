
file =open("teest.txt","r")
print(file.read())


try:
    f = open("teest.txt","r")
    print(f.read())
except FileNotFoundError:
    print("Error:File not Found")
else:
    f.close()

#Read a file using readline in python

"""
try:
    f = open("test.txt","r")
    #print(f.readline())
    #print(f.readline(11))
    print(f.readlines())
    
except FileNotFoundError:
    print("Error:File not Found")
else:
    f.close()

"""

#looping through the lines
"""
try:
    f = open("test.txt","r")
    for line in f:
        print(line)
    
except FileNotFoundError:
    print("Error:File not Found")
else:
    f.close()
"""
#write to an  existing

"""
try:
    f = open("test.txt","w")
    f.write("This is kamesh kumar from home")
    f.close()

    f = open("test.txt","r")
    for line in f:
        print(line)
    
except FileNotFoundError:
    print("Error:File not Found")
else:
    f.close()
"""
#append

"""
try:
    f = open("test.txt","a")
    f.write("I need job please")
    f.close()

    f = open("test.txt","r")
    print(f.read())
    
except FileNotFoundError:
    print("Error:File not Found")
else:
    f.close()

"""
#Delete File

import os
if os.path.exists("test.txt"): 
    os.remove("test.txt")
    os.rmdir("folder name")
else:
    print("file not found")
