from django.urls import path
from .views import upload_employees

urlpatterns = [
    path('upload-employees/', upload_employees, name='upload_employees'),
]
