employees = []

def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")

    employees.append({
        "ID": emp_id,
        "Name": name,
        "Department": department
    })

    print("Employee added successfully.")

def view_employees():
    if not employees:
        print("No employee records found.")
        return

    for emp in employees:
        print(emp)

def search_employee():
    emp_id = input("Enter Employee ID: ")

    for emp in employees:
        if emp["ID"] == emp_id:
            print(emp)
            return

    print("Employee not found.")

def delete_employee():
    emp_id = input("Enter Employee ID: ")

    for emp in employees:
        if emp["ID"] == emp_id:
            employees.remove(emp)
            print("Employee deleted.")
            return

    print("Employee not found.")

while True:
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        search_employee()
    elif choice == "4":
        delete_employee()
    elif choice == "5":
        break
