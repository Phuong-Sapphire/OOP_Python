# class Mammal:
#     def mammal_info(self):
#         print("Mammals can give the direct birth")
#
#
# class WingedAnimal:
#     def winged_animal_info(self):
#         print("Winged animal can flap")
#
#
# class Bat(Mammal, WingedAnimal):
#     pass
#
#
# bat1 = Bat()
# bat1.mammal_info()
# bat1.winged_animal_info()

class A:
    def process(self):
        print('A process()')


class B:
    def process(self):
        print('B process()')


class C(A, B):
    def process(self):
        print('C process()')


class D(C,B):
    pass


obj = D()
obj.process()

print(D.mro())