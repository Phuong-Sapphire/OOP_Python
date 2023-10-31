class Book:
    def __init__(self, id, name, publisher, number_of_page, cost):
        self.id = id
        self.name = name
        self.publisher = publisher
        self.number_of_page = number_of_page
        self.cost = cost

    def input(self):
        self.id = input("nhập mã sách: ")
        self.name = input("nhập tên sách: ")
        self.publisher = input("nhập nhà xuất bản: ")
        self.number_of_page = input("nhập số trang: ")
        self.cost = input("nhập giá tiền: ")

    def output(self):
        print(f"mã sách: {self.id}")
        print(f"tên sách: {self.name}")
        print(f"nxb: {self.publisher}")
        print(f"số trang: {self.number_of_page}")
        print(f"giá tiền: {self.cost}")


books = []
number = int(input("nhập số lượng sách: "))
for i in range(number):
    i = Book("","","", 0, 0)
    i.input()
    books.append(i)

for y in range(len(books)):
    books[y].output()
