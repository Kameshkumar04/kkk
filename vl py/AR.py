para=[]
print("Enter your details : ")

while True:
    lines=input()
    if lines():
      para.append(lines)
    else:
      break
print("\n".join(para))