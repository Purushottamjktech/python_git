import self as self
class Employee:

    company = "GOOGLE"

    def __init__(self,name,department):
        self.name = name
        self.department = department

    def edetails(self):
        print(f"Name of employee is {self.name}  and he is working in {self.company}  in {self.department} section")


a = Employee("PURUSHOTTAM","DEVELOPER")
b = Employee("PALLAVI","TRAINING")


a.edetails()
b.edetails()






