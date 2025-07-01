# ✅ Q1. Animal → Dog → Puppy
# # Q1: Create classes as follows:
# # Animal → Dog → Puppy
# # Animal has a method 'eat'
# # Dog has a method 'bark'
# # Puppy has a method 'sleep'
# # # Make object of Puppy and call all 3 methods

# class Animal:
#     def __init__(self,eat):
#         self.eat = eat
#     def show_info(self):
#         print("Animal eat", self.eat)
# class Dog(Animal):
#     def __init__(self,eat,bark):
#         super().__init__(eat)
#         self.bark = bark
#     def show_details(self):
#         print("Dog barks",self.bark)
# class Puppy(Dog):
#     def __init__(self,eat,bark,sleep):
#         super().__init__(eat,bark)
#         self.sleep = sleep
#     def show_full_info(self):
#         print("Puppy", self.sleep)
#         print("Dog",self.bark)
#         print("Animal", self.eat)
# p = Puppy("Meat","loud", "alot")
# p.show_full_info(

# # ✅ Q2. Vehicle → Car → ElectricCar
# # # Q2: Create a class Vehicle with method 'start'
# # # Car inherits Vehicle and adds method 'drive'
# # # ElectricCar inherits Car and adds method 'charge'
# class Vehicle:
#     def __init__(self,start):
#         self.start = start
#     def show_info(self):
#         print("Vehicle", self.start)
# class Car(Vehicle):
#     def __init__(self,start,drive):
#         super().__init__(start)
#         self.drive = drive
#     def show_details(self):
#         print("Car",self.drive)
# class ElectricCar(Car):
#     def __init__(self,start,drive,charge):
#         super().__init__(start,drive)
#         self.charge = charge
#     def show_info_full(self):
#         print("Vehicle", self.start)
#         print("Car",self.drive)
#         print("ElectricCar", self.charge)

# E = ElectricCar("slow","driver","battery")
# E.show_info_full()




# # Make object of ElectricCar and call all 3 methods
# ✅ Q3. Student → Graduate → MastersStudent
# python
# Copy
# Edit
# # # Q3: Create multilevel classes:
# # # Student with 'name' attribute
# # # Graduate inherits Student and adds 'degree'
# # # MastersStudent inherits Graduate and adds 'specialization'

# class Student:
#     def __init__(self,name):
#         self.name = name
#     def show_info(self):
#         print("Student",self.name)
# class Graduate(Student):
#     def __init__(self,name,degree):
#         super().__init__(name)
#         self.degree = degree
#     def show_details(self):
#         print("Graduate",self.degree)
# class MastersStudent(Graduate):
#     def __init__(self, name, degree,specialisation):
#         super().__init__(name,degree)
#         self. specialisation = specialisation
#     def show_full_info(self):
#         print("Student",self.name)
#         print("Graduate",self.degree)
#         print("MastersStudent",self.specialisation)

# ms = MastersStudent("Komal","BCA","Data Science")
# ms.show_full_info()



# ✅ Q5. Person → Employee → Manager

# Q5: Create multilevel classes:
# 1. Class Person with attribute 'name'
# 2. Class Employee inherits Person, adds 'emp_id'
# 3. Class Manager inherits Employee, adds 'department'

# Make constructor for all using super()
# Create a method in Manager class to show all information
# Create an object of Manager and display details

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

