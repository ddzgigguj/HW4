from papa_mama import*
class nomer5(nomer3,nomer4):
    def __init__(self,name,age):
        super().__init__(name)
        self.__age = age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,new_age):
        if new_age >= 0:
            self.__age = new_age
        else:
            print("Age cannot be negative")
    def method2(self):
        print("This is a method from CombinedClass")

People = nomer5("John", 30)
People.method2()
print("Name:", People.name)
print("Age:", People.age)

People.age = 25
print("Updated Age:", People.age)