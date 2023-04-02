import pandas as pd
from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from employees.models import Employee
from employees.serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ["first_name", "last_name", "gender", "years_of_experience"]

    @action(detail=False, methods=['get'], url_path='average_age_per_industry')
    def average_age(self, request):
        # Load data
        data = Employee.objects.all().values('industry', 'date_of_birth')
        df = pd.DataFrame.from_records(data)
        # Cleanup data
        df.dropna(inplace=True)
        df = df[df['industry'] != 'n/a']
        # Transform dob data and compute the number of years.
        df['date_of_birth'] = pd.to_datetime(df['date_of_birth'], format='%Y-%m-%d')
        df['age'] = (pd.to_datetime('today') - df['date_of_birth']).astype('<m8[Y]')
        # Group data by industry and compute the mean rounded by 2 decimal points on the salary column
        avg_age_per_industry = df.groupby('industry')['age'].mean().round().reset_index()
        return Response(data=avg_age_per_industry.to_dict('records'))

    @action(detail=False, methods=['get'], url_path='average_salary_per_industry')
    def average_salary_on_industry(self, request):
        # Load data
        data = Employee.objects.all().values('industry', 'salary')
        df = pd.DataFrame.from_records(data)
        # Cleanup data
        df.dropna(inplace=True)
        df = df[df['industry'] != 'n/a']
        # Group data by industry and compute the mean rounded by 2 decimal points on the salary column
        avg_salary_per_industry = df.groupby('industry')['salary'].mean().round(2).reset_index()
        return Response(data=avg_salary_per_industry.to_dict('records'))

    @action(detail=False, methods=['get'], url_path='average_salary_per_years')
    def average_salary_on_years(self, request):
        data = Employee.objects.all().values('years_of_experience', 'salary')
        df = pd.DataFrame.from_records(data)
        # Cleanup data
        df.dropna(inplace=True)

        avg_salary_per_experience = df.groupby('years_of_experience')['salary'].mean().round(2).reset_index()
        return Response(data=avg_salary_per_experience.to_dict('records'))

    @action(detail=False, methods=['get'], url_path='gender_distribution')
    def gender_distribution_on_industry(self, request):
        data = Employee.objects.all().values('industry', 'salary', 'gender', 'id')
        df = pd.DataFrame.from_records(data)

        # Cleanup data
        df.dropna(inplace=True)

        # Group the dataframe by industry and gender, and compute the mean salary and count for each group
        grouped = df.groupby(['industry', 'gender']).agg({'salary': 'mean', 'id': 'count'})

        # Compute the total count of employees for each industry
        total_count = grouped.groupby(['industry']).agg({'id': 'sum'})

        # Compute the percentage of males and females for each industry
        grouped['percentage'] = grouped['id'] / total_count['id'] * 100

        # Reset the index of the grouped dataframe to make it easier to work with
        grouped = grouped.reset_index()

        # Create a list of dictionaries with the results for each industry
        result = []
        for industry in grouped.industry.unique():
            industry_data = {'industry': industry}
            for gender in ['M', 'F']:
                gender_data = grouped[(grouped.industry == industry) & (grouped.gender == gender)]
                if not gender_data.empty:
                    gender_mean_salary = gender_data.iloc[0]['salary']
                    gender_percentage = gender_data.iloc[0]['percentage']
                    gender_count = gender_data.iloc[0]['id']
                else:
                    gender_mean_salary = 0
                    gender_percentage = 0
                    gender_count = 0
                industry_data[gender] = {
                    'mean_salary': round(gender_mean_salary, 2),
                    'percentage': round(gender_percentage, 2),
                    'count': gender_count
                }
            result.append(industry_data)
        return Response(data=result)
