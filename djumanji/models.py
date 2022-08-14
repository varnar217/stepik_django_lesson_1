
# Create your models here.
from django.db import models

# from djumanji.data import specialties, companies, jobs


class Company(models.Model):
    name = models.CharField(max_length=32)
    location = models.CharField(max_length=32, default='')
    logo = models.CharField(max_length=200, default='')
    description = models.CharField(max_length=200, default='')
    employee_count = models.IntegerField(null=True, default=0)

    class Meta:
        app_label = 'djumanji'


class Specialty(models.Model):
    code = models.CharField(max_length=32)
    title = models.CharField(max_length=50, default='')
    picture = models.CharField(max_length=200, default='')

    class Meta:
        app_label = 'djumanji'


class Vacancy(models.Model):
    title = models.CharField(max_length=64)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.CharField(max_length=200, default='')
    salary_min = models.IntegerField(null=True, default=0)
    salary_max = models.IntegerField(null=True, default=0)
    published_at = models.CharField(max_length=200, default='')

    class Meta:
        app_label = 'djumanji'


# скрипт добавления данных из файла data.py
'''
for spec in specialties:
    try:
        Specialty.objects.get(code=spec['code'])
    except Specialty.DoesNotExist:
        Specialty.objects.create(code=spec['code'], title=spec['title'], picture='https://place-hold.it/100x60')
        print(spec['code'], '- Добавлено успешно')
    else:
        print(spec['code'], '- уже находится в базе данных')


for company in companies:
    try:
        Company.objects.get(name=company['title'])
    except Company.DoesNotExist:
        Company.objects.create(name=company['title'], logo='https://place-hold.it/100x60')
        print(company['title'], '- Добавлено успешно')
    else:
        print(company['title'], '- уже находится в базе данных')


for job in jobs:
    spec = Specialty.objects.get(code=job['cat'])
    company_key = Company.objects.get(name=job['company'])
    Vacancy.objects.create(title = job['title'],
            specialty = spec,
            company = company_key,
            skills = job['desc'],
            salary_min = job['salary_from'],
            salary_max = job['salary_to'],
            published_at = job['posted'])
    print(job['title'], '- Добавлено успешно')'''
