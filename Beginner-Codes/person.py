class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def say_name(self):
        print(f"Hi many name is {self.name}")
    
    def say_age(self):
        print(f"My age is {self.age}")


person1 = Person("Phuoc", 22)

Person.say_name(person1)
Person.say_age(person1)


