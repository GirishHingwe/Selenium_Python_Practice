class employee1():
    def name(self):
        print("Harshit is his name")
    def salary(self):
        print("3000 is his salary")
    def age(self):
        print("22 is his age")

class employee2(employee1):
    def m1(self):
        print("hello")
        super().salary()
    def salary(self):
        print("New Salary is 5000")
emp2 = employee2()
emp2.m1()
emp2.salary()
emp2.age()
emp2.name()
emp1=employee1()
emp1.name()
emp1.age()
emp1.salary()