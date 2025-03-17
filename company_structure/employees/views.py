from django.shortcuts import render
from django.http import JsonResponse
from .models import Department

def department_tree(request):
    def build_tree(department):
        return {
            'id': department.id,
            'name': department.name,
            'employees': list(department.employees.values('full_name', 'position', 'hire_date', 'salary')),
            'children': [build_tree(child) for child in department.children.all()]
        }
    root_departments = Department.objects.filter(parent__isnull=True)
    tree = [build_tree(dept) for dept in root_departments]
    return JsonResponse(tree, safe=False)
