
class Employee:
    def __init__(self, name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: ${self.salary}"
    
    def __repr__(self):
        return f"Employee(name='{self.name}', age={self.age}, salary={self.salary})"

class EmployeesRepository:
    def __init__(self):
        self.employees = []
    
    def add_employee(self, name, age, salary):
        self.employees.append(Employee(name, age, salary))
    
    def get_all_emps(self):
        return self.employees
    
    def delete_age_range(self, f,t):
        deleted_emps = []
        i = 0
        while i < len(self.employees):
            if (f <= self.employees[i].age <= t):
                self.employees[i], self.employees[-1] = self.employees[-1], self.employees[i]
                deleted_emps.append(self.employees.pop())
                continue
            i += 1
        return deleted_emps
    
    def update_salary(self, name, new_salary):
        for emp in self.employees:
            if emp.name == name:
                emp.salary = new_salary
                return True
        return False
    
    def check_emp_exist(self,name):
        for emp in self.employees:
            if emp.name == name:
                return True
        return False

class FactoryFrontend:
    def show_options(self):
        print("Factory Options:")
        print("1) Add a new employee")
        print("2) List all employees")
        print("3) Delete by age range")
        print("4) Update salary given a name")
        print("5) End the Program")
        choice = 0
        while True:
            choice = int(input("Enter your choice (from 1 to 5): "))
            if 0 < choice < 6:
                break
            else: print("Invalid option choose correctly from the options!")
        return choice
    
    def show_new_emp_form(self):
        print("\nEnter employee data:\n")
        name = input("Enter the name: ")
        age = int(input("Enter the age: "))
        salary = float(input("Enter the salary: "))
        return name,age,salary
    
    def list_all_emps(self, emps):
        print("\nEmployees List:\n")
        for emp in emps:
            print(f"\t{emp}")
        print()

    def show_delete_emps_form(self):
        print("\nDelete employees by age range:")
        f = int(input("From age: "))
        t = int(input("To age: "))
        return f,t
    
    def show_deleted_emps(self, deleted_emps):
        print("\n Deleted employees:")
        for emp in deleted_emps:
            print(f"\t{emp}")
        print()

    def show_update_emps_form(self):
        print("\nUpdate Employee Salary:")
        name = input("Employee name: ")
        new_salary = float(input("New Salary: "))
        return name, new_salary

    def show_message(self, msg):
        print(f"\n{msg}\n")

class FactoryController:
    def __init__(self):
        self.ui = FactoryFrontend()  
        self.employees_repository = EmployeesRepository()  
    
    def handle_new_employee(self):
        emp_data = self.ui.show_new_emp_form()
        self.employees_repository.add_employee(*emp_data)
        self.ui.show_message("Employee added successfully!")

    def handle_list_all_employees(self):
        self.ui.list_all_emps(self.employees_repository.get_all_emps())

    def handle_delete_age_range_emps(self):
        f,t = self.ui.show_delete_emps_form()
        deleted_emps = self.employees_repository.delete_age_range(f,t)
        self.ui.show_deleted_emps(deleted_emps)

    def handle_update_emp_salary(self):
        name, new_salary = self.ui.show_update_emps_form()
        emp_exists = self.employees_repository.check_emp_exist(name)
        if emp_exists == False:
            self.ui.show_message("Employee doesn't exist!")
        else:
            self.employees_repository.update_salary(name, new_salary)
            self.ui.show_message("Employee salary updated successfully!")

    def init(self):
        while True:
            choice = self.ui.show_options()
            if (choice == 1):
                self.handle_new_employee()
            elif choice == 2:
                self.handle_list_all_employees()
            elif choice == 3:
                self.handle_delete_age_range_emps()
            elif choice == 4:
                self.handle_update_emp_salary()
            elif choice == 5:
                self.ui.show_message("Bye!")
                return
    
app = FactoryController()
app.init()
