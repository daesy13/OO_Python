class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@levelup.com"
        self.pay = pay

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay =  int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.10
    """docstring for Developer"""
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.fullname())


#****this will let you see a mapping of that specific class ***
# print(help(Developer))

# emp_1 = Employee("Daesy", "Stephens", 150000)
# emp_2 = Employee("Jhon", "Doe", 125000)

# print(emp_1.email)
# print(emp_2.email)

dev_1 = Devloyee("Daesy", "Stephens", 150000, "Python")
dev_2 = Devloyee("Jhon", "Doe", 125000, "Java")

mgr_1 = Manager("Sue", "Smith", 200000, [dev_1])

#********TEST CASE********
print(isinstance(mgr_1, Employee))#True
print(isinstance(mgr_1, Developer))#False

print(issubclass(Developer, Employee))#True
print(issubclass(Manager, Developer))#False


print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.print_emps()

mgr_1.remove_emp(dev_2)
mgr_1.print_emps()

# print(dev_1.email)
# dev_1.apply_raise()
# print(dev_1.prog_lang)