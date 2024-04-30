from pytest import approx
from employee_info import get_employees_by_age_range, calculate_average_salary, get_employees_by_dept

def test_get_employees_by_age_range():
    age_lower = 25
    age_upper = 35
    expected_result = {
        
        ("John", 30, "Sales", 50000),
        ("Mike", 32, "Engineering", 65000)
    }
    actual_result = {(emp["name"], emp["age"], emp["department"], emp["salary"]) for emp in get_employees_by_age_range(age_lower, age_upper)}
    assert actual_result == expected_result


def test_calculate_average_salary():
    expected_average_salary = 60166.666666666664
    assert calculate_average_salary() == approx(expected_average_salary, abs =1)

def test_get_employees_by_dept():
    department = "Sales"
    expected_result = [
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
    ]
    actual_result = get_employees_by_dept(department)
    assert actual_result == expected_result

