class Person:
    def __init__(self,name):
        self.name = name
    def show_info(self):
        print("Name",self.name)
class Employee(Person):
    def __init__(self,name,emp_id):
        super().__init__(name)
        self.emp_id = emp_id
    def show_details(self):
        print("Emp_Id", self.emp_id)
class Manager(Employee):
    def __init__(self, name, emp_id,department):
        super().__init__(name,emp_id)
        self.department = department
    def show_full_info(self):
        print("Name",self.name)
        print("Emp_Id", self.emp_id)
        print("Department", self.department)

m = Manager("Kavyansh",111,"Accounts")
m.show_full_info()

