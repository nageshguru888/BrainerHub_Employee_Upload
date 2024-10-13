from rest_framework import serializers
from .models import Company, Employee


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name']


class EmployeeSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'company', 'salary', 'manager_id', 'department_id']

    def create(self, validated_data):
        company_data = validated_data.pop('company')
        company, created = Company.objects.get_or_create(name=company_data['name'])
        employee = Employee.objects.create(company=company, **validated_data)
        return employee        