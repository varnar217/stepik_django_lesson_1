
"""Stepik_django_week3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.urls import re_path

from djumanji.views import my_custom_page_404
from djumanji.views import my_custom_page_500
from djumanji.views import VacanciesView
from djumanji.views import MainView
from djumanji.views import CompaniesView
from djumanji.views import CategoryView


urlpatterns = [
    path('', MainView.as_view()),
    path('vacancies/cat/<str:cat>', CategoryView.as_view()),
    re_path(r'^vacancies/?(?P<id>\d*)?', VacanciesView.as_view()),
    path('companies/<int:id>/', CompaniesView.as_view()),
]

handler404 = my_custom_page_404
handler500 = my_custom_page_500
