from django.contrib import admin
from .models import Employee, Company


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'company', 'salary')
    search_fields = ('first_name', 'last_name', 'company_name')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name')
    search_fields = ('company_name',)
