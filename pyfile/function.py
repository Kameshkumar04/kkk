"""
def kamesh():
    print("hello world!")
kamesh()

def placements(a,b):
    if a>b:
        print("a is graeterb than b")
placements("20","10")

x = ['ab', 'cd']
for i in x:
    i.upper()
print(x)

i = 1
while True:
    i+=1
    if i % 3 == 0:
        break
    print(i)

x = ['ab', 'cd']
for i in x:
    i.upper()
print(x)

fruits=["apple","Mango","banannan","Kiwi"]
Newfruits = []
for i in fruits:
    if "w" in i:
        Newfruits.append(i)
print(Newfruits)

fruits=["apple","Mango","banannan","Kiwi"]
Newfruits = [i for i in fruits if "w" in i]
print(Newfruits)
"""
#read
""""
f = open("error2.txt","r")
print(f.readline())
print(f.readline())
print(f.close())
"""
#append
"""
f = open("error2.txt","a")
f.write("  A new files open  ")
f.close()
f = open("error2.txt","r")
print(f.read())
"""
#write
"""
f = open("error2.txt","w")
f.write("  A new files open  ")
f.close()
f = open("error2.txt","r")
print(f.read())
"""
#create
#f = open("kamesh.txt","x")

"""
#remove
import os
if os.path.exists("kamesh.txt"):
    os.remove("kamesh.txt")
else:
    print("file not presents")
"""

