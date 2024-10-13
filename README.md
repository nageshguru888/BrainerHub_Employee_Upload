# Employee Management System

A Django-based web application that allows uploading employee data via a CSV file. This project reads the uploaded CSV file and inserts the data into two related tables: `Employee` and `Company`.

## Features

- Upload employee data via a CSV file
- Store employee details such as first name, last name, phone number, salary, manager ID, department ID
- Automatically handles related `Company` information and ensures no duplicate companies are created
- Bulk creation of `Employee` and `Company` instances for efficiency

## Prerequisites

- Python 3.8+
- Django 3.0+
- pandas (for reading CSV files)
- Django Rest Framework (if you want to extend this to API functionality)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/nageshguru888/Brainerhub_Employee_Upload.git
   cd Company_Employee
