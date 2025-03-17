import os
import django
# Указываем Django, где находятся настройки проекта
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "company_structure.settings")
django.setup()
import random
from faker import Faker
from django.db import transaction
from employees.models import Department, Employee

fake = Faker()



def create_departments():
    departments = []
    for i in range(5):
        dept = Department.objects.create(name=f'Department Level 1-{i}')
        departments.append(dept)
        for j in range(5):
            sub_dept = Department.objects.create(name=f'Department Level 2-{i}-{j}', parent=dept)
            departments.append(sub_dept)
            for k in range(5):
                sub_sub_dept = Department.objects.create(name=f'Department Level 3-{i}-{j}-{k}', parent=sub_dept)
                departments.append(sub_sub_dept)
    return departments

def create_employees(departments):
    with transaction.atomic():
        for _ in range(50000):
            Employee.objects.create(
                full_name=fake.name(),
                position=fake.job(),
                hire_date=fake.date_between(start_date='-10y', end_date='today'),
                salary=random.randint(30000, 150000),
                department=random.choice(departments)
            )

def populate_database():
    departments = create_departments()
    create_employees(departments)

if __name__ == "__main__":
    populate_database()
