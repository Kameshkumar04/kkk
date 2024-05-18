"""
s = "Python Programming"
print(s[::])
#List
List1=[1,2,3,4,5]
print(List1*3)
print(type(List1))
List1[3]=10
print(List1)
#Index
fruits =["Apple","Mango","Banana","Grapes","Orange","Grapes","Orange","Orange","Orange"]
fruits1 =["Apple","Mango","Banana","Grapes","Orange","Grapes",]
fruits2 =["Jackfruits","Watermelon"]

a=fruits1 +fruits2
print(a)
print(fruits.index("Orange"))
print(fruits.count("Orange"))
fruits1.extend(fruits2)
print(fruits1)
fruits1.append(fruits2)
print(fruits1)

fruits1.reverse()
print(fruits1)

fruits.remove("Orange")
print(fruits)

fruits.pop(0)
print(fruits)

fruits.insert(0,"cherry")
print(fruits)
"""

a="Apple",12,12.5,"1+2j"
print(a)
print(type(a))

firstname = ("Arun","Ajay","Tharun","Vijay")
lastname = ("Kumar","Kishan","Santhosh","Kumar")
age = (25,30,32,27)
result = (firstname,lastname,age)
print(result)
print(result[2][2])

