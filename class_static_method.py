from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birthday(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def is_adult(age):
        return age > 18


person = Person("Phuong", 22)
person1 = Person.from_birthday("Sapphire", 2002)

print(person.age)
print(person1.age)
print(Person.is_adult(17))