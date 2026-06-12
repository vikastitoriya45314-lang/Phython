class Employee:
    def __init__(self):
        self.__salary = 50000

    def increment(self):
        self.__salary = 10000

    def deduct(self):
        self.__salary = 5000

    def get_salary(self):
        print("Salary:", self.__salary)

Employee1 = Employee()
Employee2 = Employee()
print("Employee 1")
Employee1.get_salary()
Employee1.increment()
Employee1.get_salary()
Employee1.deduct()
Employee1.get_salary()
print("\nEmployee 2")
Employee2.get_salary()
Employee2.increment()
Employee2.get_salary()
Employee2.deduct()
Employee2.get_salary()