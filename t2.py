class Person:
    def set_name(self,name):
        self.name = name
    def set_surname(self, surname):
        self.surname = surname

p1 = Person()
print(p1)
p1.surname('Kalynovskyi')
print(p1.surname)

p2 = Person()
print(p2)
p1.surname('Shovkun-Kalynovsksaya')
print(p2.surname)