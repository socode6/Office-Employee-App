from django.contrib import admin
from .models import Department, Roles, Employee

admin.site.register(Department)
admin.site.register(Roles)
admin.site.register(Employee)