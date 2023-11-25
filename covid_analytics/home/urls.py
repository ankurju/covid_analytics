from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='homepage'),
    path('deaths/',views.fetch_deaths_data,name='deaths'),
    path('cases/',views.fetch_cases_data,name='cases'),
    path('vaccinations/',views.fetch_vaccinations_data,name='vaccinations'),
    path('hospitalizations/',views.fetch_hospitalizations_data,name='hospitalizations'),
    path('redirect_plot_page/', views.redirect_plot_page, name='redirect_plot_page'),
]