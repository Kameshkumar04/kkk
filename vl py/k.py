def add(a,b):
    c=a+b
    print(c)
a1 = int(input("Enter number A: "))
b1 = int(input("Enter number B: "))
add(a1,b1)


def details(*data):
    print(data)
details("kamesh",23,101)