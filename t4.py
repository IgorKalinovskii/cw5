class Person:
    def __init__(self, name = None, surname = None, age = 0):
        self.name = name
        self.surname = surname
        self.age = age
    def full_name(self):
         # return str(self.name) + ' ' + str(self.surname)

         # return "{} {}".format(self.name, self.surname)

        return f"{self.name} {self.surname}"
    def get_older(self, years):
        self.age += int(years)
    def __str__(self):
         return f" {self.__class__}  object   {self.name} {self.surname}"

class Employee(Person):
    """  """
    def __init__(self,  name = None, surname = None, age = 0, salary=0, position=None):
        # self.name = name
        # self.surname = surname
        # self.age = age
        # self.skills = []
        # super().__init__(name, surname, age,
        #                  skills)
        if skills is not None:
            self.skills.extend(skills)
        self.salary = salary
        self.position = position
    def income(self, months):
        return self.salary * months


class ITEmployee(Employee):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.skills = []

    def add_skills(self, skills):
        self.skills.extend(skills)

    def add_skill(self, skill):
        self.skills.append(skill)

    def __add__(self, other):
        return self.skills + other.skills
    



e2 = ITEmployee()
# p1 = Person('Vasya','Vasiliev', 25)
# print(p1.name, p1.surname, p1.age)
# print(p1.full_name())

# p2 = Employee()
# print(p2.name, p2.surname, p2.age)
# print(p2.full_name())
#
#
# print(p2.age)
# p2.get_older(20)
# print(p2.age)
# p1.get_older(100)
# print(p1.age)
#
# print(p1)
# print(p2)

