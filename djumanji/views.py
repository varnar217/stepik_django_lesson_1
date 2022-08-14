
from django.shortcuts import render
from django.http import Http404
from django.views import View
# from django.db.models import Avg, Count, Sum

from djumanji.models import Vacancy, Company, Specialty

companies = Company.objects.all()
specialities = Specialty.objects.all()
vacancys = Vacancy.objects.all()

# Create your views here.


class MainView(View):
    def get(self, request):
        context = {
            'companies': companies,
            'specialities': specialities
        }
        return render(request, 'djumanji/index.html', context=context)


class VacanciesView(View):
    def get(self, request, id):
        if id:
            try:
                vacancy = Vacancy.objects.get(id=id)
            except Vacancy.DoesNotExist:
                raise Http404
            else:
                context = {
                    'vacancy': vacancy
                }
                return render(request, 'djumanji/vacancy.html', context=context)

        else:
            context = {
                'vacancies': vacancys
            }
            return render(request, 'djumanji/vacancies.html', context=context)


class CompaniesView(View):
    def get(self, request, id):
        vac_by_company = Vacancy.objects.filter(company__id=id)
        vac_count = vac_by_company.count()
        try:
            company = Company.objects.get(id=id)
        except Company.DoesNotExist:
            raise Http404
        else:
            context = {
                'vacancies': vac_by_company,
                'company': company,
                'count': vac_count
            }
            return render(request, 'djumanji/company.html', context=context)


class CategoryView(View):
    def get(self, request, cat):
        vac_by_category = Vacancy.objects.filter(specialty__code=cat)
        vac_count = vac_by_category.count()
        context = {
            'vacancies': vac_by_category,
            'category': cat,
            'count': vac_count
        }
        return render(request, 'djumanji/vac_by_speciality.html', context=context)


def my_custom_page_404(request, exception=None):
    return render(request, 'djumanji/404.html')


def my_custom_page_500(request, exception=None):
    return render(request, 'djumanji/500.html')
