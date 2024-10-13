from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Company(models.Model):
    company_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.company_name



class Employee(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    phone_number = PhoneNumberField(blank=True, null=True)
    company = models.ForeignKey(Company, related_name='employees', on_delete=models.CASCADE)
    salary = models.FloatField()
    manager_id = models.IntegerField()
    department_id = models.IntegerField()
    

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.phone_number} {self.salary} {self.manager_id} {self.department_id}"

