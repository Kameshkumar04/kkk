class Contact():
    def Con_details(self):
        print("The Person Name is Alice")
class Age(Contact):
    def Age_details(self):
        print("Age is 30")
class City(Contact):
    def City_details(self):
        print("City is WonderLand")
class Person(Age,City):
    def Per_details(self):
        print("The PhoneNo is 555-12345")
ob=Person()
print("----Details----")
ob.Con_details()
ob.Age_details()
ob.City_details()
ob.Per_details()