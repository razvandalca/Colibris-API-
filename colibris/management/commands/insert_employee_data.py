import json
from datetime import datetime

from django.core.management.base import BaseCommand
from employees.models import Employee

class Command(BaseCommand):
    help = 'Insert employee data from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='JSON filename to import')

    def handle(self, *args, **options):
        if Employee.objects.exists():
            self.stdout.write(self.style.SUCCESS('Data already exists, will not import data.'))
            return

        filename = options['filename']
        with open(filename, 'r') as f:
            employees = json.load(f)
            for emp in employees:
                dob_str = emp['date_of_birth']
                dob = datetime.strptime(dob_str, '%d/%m/%Y').date()
                employee = Employee(
                    first_name=emp['first_name'],
                    last_name=emp['last_name'],
                    email=emp['email'],
                    gender=emp['gender'],
                    date_of_birth=dob,
                    industry=emp['industry'],
                    salary=emp['salary'],
                    years_of_experience=emp['years_of_experience']
                )
                employee.save()
        self.stdout.write(self.style.SUCCESS('Data inserted successfully.'))
