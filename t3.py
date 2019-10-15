class Person:
    common_properties = {'species':'human','amount': None}
    def set_name(self, value):
        self.name = value


if __name__ == '__main__':
    p1 = Person()
    p1.set_name('Vasya')

    p2 = Person()
    p2.set_name('Kolya')

    print(p1.name, p2.name)
    print(p1.common_properties)
    print(p2.common_properties)
    print(p1.common_properties is p2.common_properties)

    p1.common_properties['amount'] = 9e9

    print(p1.common_properties)
    print(p2.common_properties)


# class Person:
#     def __init__(self, name, surname,age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#
#
#
# p1 = Person('Vasya','Vasiliev', 25)
# print(p1.name, p1.surname, p1.age)