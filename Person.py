class Person:
    def __init__(self, name, dob, address):
        self.name = name
        self.dob = dob
        self.address = address


class Engineer(Person):
    def __init__(self, name, dob, que_quan, major, year_of_graduation):
        super().__init__(name, dob, que_quan)
        self.major = major
        self.year_of_graduation = year_of_graduation

    def input(self):
        self.name = input("enter name: ")
        self.dob = input("enter date of birth: ")
        self.address = input("enter address: ")
        self.major = input("enter major: ")
        self.year_of_graduation = input("enter year of graduation: ")

    def output(self):
        print(f"name: {self.name}")
        print(f"date of birth: {self.dob}")
        print(f"address: {self.address}")
        print(f"major: {self.major}")
        print(f"year of graduation: {self.year_of_graduation}")


engineers = []
num_of_engineer = int(input("enter the number of engineers: "))
for i in range(num_of_engineer):
    i = Engineer("", "", "", "", 0)
    i.input()
    engineers.append(i)

print("==============List of engineers==================")
for i in range(len(engineers)):
    engineers[i].output()

print("==============list of engineers who have just graduated===============")
max_year = engineers[0].year_of_graduation
for i in range(1, len(engineers)):
    if engineers[i].year_of_graduation > max_year:
        max_year = engineers[i].year_of_graduation

for i in range(len(engineers)):
    if engineers[i].year_of_graduation == max_year:
        engineers[i].output()

