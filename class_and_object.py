class Student:

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    @classmethod
    def introduction(cls):
        print(f"name: {Student.name}, age: {Student.age}, address: {Student.address}")

    def get_job(self):
        if self.age <= 22:
            print("go to school or university")
        else:
            print("go to work")


student_1 = Student("Phuong", 22, "Ha Noi")
student_1.introduction()
student_1.get_job()

Student.introduction()
Student.get_job()

# class SuperHero:
#     power = 100
#
#
# super_hero1 = SuperHero()
# print(SuperHero.power)
# print(super_hero1.power)
# # change value of attribute by Class
# SuperHero.power = 200
# print(SuperHero.power)
# print(super_hero1.power)
#
# # change value of attribute by Object
# super_hero1.power = 90
# print(SuperHero.power)
# print(super_hero1.power)
