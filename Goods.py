class Goods:
    def __init__(self):
        self.items = []

    def add_item(self, id_item, name_item, unit, quantity):
        item = [id_item, name_item, unit, quantity, unit*quantity]
        self.items.append(item)

    def total_amount(self):
        total = 0
        for i in self.items:
            total += i[4]

        return total


goods = Goods()
goods.add_item("id01", "book", 5000, 2)
goods.add_item("id02", "pencil", 2000, 4)
goods.add_item("id03", "erase", 1000, 9)


print("============list of goods=============")
for i in goods.items:
    print(f"id: {i[0]}, name: {i[1]}, unit: {i[2]}, quantity: {i[3]}, amount: {i[4]}")


total_amount = goods.total_amount()
print(f"total amount: {total_amount}")