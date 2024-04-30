# Define a dictionary to store employee information
employee_data = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    {"name": "Chloe", "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
]

def get_employees_by_age_range(age_lower_limit, age_upper_limit):
    result = []

    # check for age limits and append the item to result
    for item in employee_data:
        if int(item["age"]) > int(age_lower_limit) and int(item["age"]) < int(age_upper_limit):
            result.append(item)

    return result

def calculate_average_salary():
    total = sum(employee["salary"] for employee in employee_data)
    return total / len(employee_data)

def get_employees_by_dept(department):
    return [employee for employee in employee_data if employee["department"] == department]

def display_all_records():
    print("Name\tAge\tDepartment\tSalary")
    for item in employee_data:
        print(f"{item['name']}\t{item['age']}\t{item['department']}\t{item['salary']}")

def display_records(employee_info):
    print("Name\tAge\tDepartment\tSalary")
    for item in employee_info:
        print(f"{item['name']}\t{item['age']}\t{item['department']}\t{item['salary']}")

def display_main_menu():
    print("\n----- Employee information Tracker -----")
    print("Select option\n")
    print("1 - Display all records")
    print("2 - Display average salary")
    print("3 - Display employee within age range")
    print("4 - Display employee in a department")
    print("Q - Quit")

    option = input("Enter selection =>").strip().upper()

    if option == '1':
        display_all_records()

    elif option == '2':
        average_salary = calculate_average_salary()
        print(f"Average salary = {average_salary}")

    elif option == '3':
        age_lower_limit = int(input("age (Lower Limit) = "))
        age_upper_limit = int(input("age (Upper Limit) = "))
        employee_info = get_employees_by_age_range(age_lower_limit, age_upper_limit)
        display_records(employee_info)

    elif option == '4':
        department = input("Name of Department = ")
        employee_info = get_employees_by_dept(department)
        display_records(employee_info)

    elif option == 'Q':
        quit()

def main():
    while True:
        display_main_menu()

if __name__ == "__main__":
    main()
