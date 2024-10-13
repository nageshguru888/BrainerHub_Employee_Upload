from django.shortcuts import render
from .models import Employee, Company
from .serializers import EmployeeSerializer
from django.http import JsonResponse
import pandas as pd


def upload_employees(request):
    if request.method == 'POST':
        file = request.FILES.get('file')

        if not file:
            return JsonResponse({"error": "File not provided."}, status=400)

        try:
            df = pd.read_csv(file)
        except Exception as e:
            return JsonResponse({"error": f"Error reading file: {str(e)}"}, status=400)

        
        company_names = df['COMPANY_NAME'].unique()
        Company.objects.bulk_create([Company(name=name) for name in company_names])

        
        employee_objects = []
        for index, row in df.iterrows():
            employee_data = {
                "first_name": row['FIRST_NAME'],
                "last_name": row['LAST_NAME'],
                "phone_number": row['PHONE_NUMBER'],
                "company": {"name": row['COMPANY_NAME']},
                "salary": row['SALARY'],
                "manager_id": row['MANAGER_ID'],
                "department_id": row['DEPARTMENT_ID'],
            }
            serializer = EmployeeSerializer(data=employee_data)
            if serializer.is_valid():
                employee_objects.append(serializer)

       
        Employee.objects.bulk_create([s.save() for s in employee_objects])

        return JsonResponse({"message": "Data successfully uploaded!"}, status=201)

    return JsonResponse({"error": "Invalid request method."}, status=405)
