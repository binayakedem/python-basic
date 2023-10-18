# class Father:
#     car="ferrari"
# class Son(Father):
#     electronics="ggc9"

# son=Son()
# print(son.car)
# print(son.electronics)

# multilevel inheritance
# class Grandfather:
#     house="Luxery house"
# class Father(Grandfather):
#     car="ferrari"
# class Son(Father):
#     electronics="ggc9"

# son=Son()
# print(son.car)
# print(son.electronics)
# print(son.house)

# multiple inheritance

# class Grandfather:
#     house="Luxery house"
# class Mother:
#     jewellary="Gold is best jewellary ever "
# class Father(Grandfather):
#     car="ferrari"
# class Son(Father,Mother):
#     electronics="ggc9"

# class Girl(Father,Mother):
#     glass="sun glass "
# girl=Girl()
# print(girl.car)
# son=Son()
# print(son.car)
# print(son.jewellary)

# method overloading
class Grandfather:
    def __init__(self) -> None:
        print("Grandfather has luxery house")
    house="Luxery house"
class Father(Grandfather):
    def __init__(self):
        print("Fathere has 9bhk house")
    car="ferrari"
# class Mother:
#     jewellary="Gold is best jewellary ever "
class Son(Father):
    def __init__(self):
        print("Bought two house")
        super().__init__()
    electronics="ggc9"

son=Son()
father=Father()
print(isinstance(son,Father))
# print(son.car)
# print(son.electronics)


