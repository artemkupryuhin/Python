class Employee:
    """
    Doc 0.0
    """
    raise_amount = 10
    num_of_obj = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_obj += 1

    def fullname(self):
        print(f'{self.first} {self.last}')

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)


emp_1 = Employee("User1", "Test1", 1000)
emp_2 = Employee("User2", "Test2", 2000)

emp_1.raise_amount = 1.10
emp_1.apply_raise()
emp_2.apply_raise()

print(Employee.__dict__)
print(emp_1.__dict__)
print(emp_2.__dict__)