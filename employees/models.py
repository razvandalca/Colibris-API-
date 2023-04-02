from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    gender = models.CharField(max_length=1, null=True, blank=True)
    date_of_birth = models.DateField()
    industry = models.CharField(max_length=255, null=True, blank=True)
    salary = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    years_of_experience = models.PositiveIntegerField(null=True, blank=True,validators=[MinValueValidator(0), MaxValueValidator(100)])
