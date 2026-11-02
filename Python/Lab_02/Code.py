Employee_name = input("Enter employee name: ")
print("Employee Name: " + Employee_name, type(Employee_name))


Employee_id = int(input("Enter employee ID: "))
print("Employee ID: " + str(Employee_id), type(Employee_id))


Employee_salary = float(input("Enter employee salary: "))
print("Employee Salary: " + str(Employee_salary), type(Employee_salary))


Employee_department = input("Enter employee department: ")
print("Employee Department: " + Employee_department, type(Employee_department))




def box(title, lines):
    print("\n" + "=" * 50)
    print(f"{title:^50}")
    print("=" * 50)
    for line in lines:
        print(f"{line:^50}")

box("Employee Details", [
    f"Employee Name: {Employee_name}",
    f"Employee ID: {Employee_id}",
    f"Employee Salary: {Employee_salary}",
    f"Employee Department: {Employee_department}"
])
print("=" * 50 + "\n")
