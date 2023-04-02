# Generated by Django 4.1.7 on 2023-04-02 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('gender', models.CharField(blank=True, max_length=1, null=True)),
                ('date_of_birth', models.DateField()),
                ('industry', models.CharField(blank=True, max_length=255, null=True)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('years_of_experience', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
