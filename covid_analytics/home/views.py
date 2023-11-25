from django.shortcuts import render,redirect
import matplotlib.pyplot as plt
import io
import urllib
import base64
from django.urls import reverse

from .script.script import process_deaths_cases_data
from .script.script import process_vaccination_data
from .script.script import process_hospitalization_data
from .constants.constants import COUNTRIES_CASE,COUNTRIES_DEATH,COUNTRIES_HOSPITALIZATION,COUNTRIES_VACCINATION

# matplotlib.use('Agg') is used to avoid some of the issues associated with running Matplotlib in a non-GUI environment.
import matplotlib
matplotlib.use('Agg')

# Create your views here.
def home(request):
    background_image_url='images/covidbanner.jpg' 
    return render(request,'home/home.html',{'background_image_url': background_image_url})

def fetch_cases_data(request):
    csv_file_path = "static/data/full_data_deaths.csv"
    countries = COUNTRIES_CASE

    total_cases_by_country_and_year, total_deaths_by_country_and_year, available_years,overall_total_cases_by_country,overall_total_deaths_by_country = process_deaths_cases_data(
        csv_file_path, countries
    )
    available_years.sort()

    plot_data_cases_combined = {}
    for year in available_years:
        # Plot for combined Cases
        plt.figure(figsize=(8, 6))
        for country in countries:
            plt.plot(total_cases_by_country_and_year[country][year].keys(), total_cases_by_country_and_year[country][year].values(),label=country)
        plt.title('Monthly Cases')
        plt.xlabel('Month')
        plt.ylabel('Total Cases')
        plt.xticks(rotation=45, ha='right')

        buffer = io.BytesIO()
        plt.legend(countries)
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        plot_data_cases_combined[year] = urllib.parse.quote(base64.b64encode(buffer.read()).decode())
        plt.close()

    countryData = []
    for country in countries:
        plot_data_cases = {}
        for year in available_years:
        # Plot for total cases
            plt.figure(figsize=(8, 6))
            plt.bar(total_cases_by_country_and_year[country][year].keys(), total_cases_by_country_and_year[country][year].values())
            plt.title(f'Monthly Cases - {country}')
            plt.xlabel('Month')
            plt.ylabel('Total Cases')
            plt.xticks(rotation=45, ha='right')

            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            plot_data_cases[year] = urllib.parse.quote(base64.b64encode(buffer.read()).decode())
            plt.close()

        countryData.append({
            'countryName': country,
            'total_cases': overall_total_cases_by_country[country],
            'plot_data_cases': plot_data_cases,
        })

    context = {
        'countryData':countryData,
        'available_years':available_years,
        'plot_data_cases_combined':plot_data_cases_combined
    }
    return render(request,'home/cases.html',context)

def fetch_deaths_data(request):
    csv_file_path = "static/data/full_data_deaths.csv"
    countries = COUNTRIES_DEATH

    total_cases_by_country_and_year, total_deaths_by_country_and_year, available_years,overall_total_cases_by_country,overall_total_deaths_by_country = process_deaths_cases_data(
        csv_file_path, countries
    )
    
    available_years.sort()

    plot_data_deaths_combined = {}
    for year in available_years:
        # Plot for combined deaths
        plt.figure(figsize=(8, 6))
        for country in countries:
            plt.plot(total_deaths_by_country_and_year[country][year].keys(), total_deaths_by_country_and_year[country][year].values(),label=country)
        plt.title('Monthly Deaths')
        plt.xlabel('Month')
        plt.ylabel('Total Deaths')
        plt.xticks(rotation=45, ha='right')

        buffer = io.BytesIO()
        plt.legend(countries)
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        plot_data_deaths_combined[year] = urllib.parse.quote(base64.b64encode(buffer.read()).decode())
        plt.close()


    countryData = []
    for country in countries:
        # Plot for total deaths
        plot_data_deaths = {}
        for year in available_years:
            plt.figure(figsize=(8, 6))
            plt.bar(total_deaths_by_country_and_year[country][year].keys(), total_deaths_by_country_and_year[country][year].values())
            plt.title(f'Monthly Deaths - {country}')
            plt.xlabel('Month')
            plt.ylabel('Total Deaths')
            plt.xticks(rotation=45, ha='right')

            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            plot_data_deaths[year] = urllib.parse.quote(base64.b64encode(buffer.read()).decode())
            plt.close()

        countryData.append({
            'countryName': country,
            'total_deaths': overall_total_deaths_by_country[country],
            'plot_data_deaths': plot_data_deaths,
        })

    context = {
        'countryData':countryData,
        'available_years':available_years,
        'plot_data_deaths_combined':plot_data_deaths_combined
    }
    return render(request,'home/deaths.html',context)

def fetch_vaccinations_data(request):
    csv_file_path= "static/data/vaccinations.csv"
    countries = COUNTRIES_VACCINATION
    total_vaccinations_by_country_and_year,overall_total_vaccinations_by_country,available_years = process_vaccination_data(csv_file_path, countries)
    
    available_years.sort()

    plot_data_vaccinations_combined = {}
    for year in available_years:
        # Plot for combined vaccinations
        plt.figure(figsize=(8, 6))
        for country in countries:
            plt.plot(total_vaccinations_by_country_and_year[country][year].keys(), total_vaccinations_by_country_and_year[country][year].values(),label=country)
        plt.title('Monthly Vaccinations')
        plt.xlabel('Month')
        plt.ylabel('Total Vaccinations')
        plt.xticks(rotation=45, ha='right')

        buffer = io.BytesIO()
        plt.legend(countries)
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        plot_data_vaccinations_combined[year] = urllib.parse.quote(base64.b64encode(buffer.read()).decode())
        plt.close()


    countryData = []
    for country in countries:
        # Plot for total vaccinations
        plot_data_vaccinations = {}
        for year in available_years:
            plt.figure(figsize=(8, 6))
            plt.bar(total_vaccinations_by_country_and_year[country][year].keys(), total_vaccinations_by_country_and_year[country][year].values())
            plt.title(f'Monthly Vaccinations - {country}')
            plt.xlabel('Month')
            plt.ylabel('Total Vaccinations')
            plt.xticks(rotation=45, ha='right')

            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            plot_data_vaccinations[year] = urllib.parse.quote(base64.b64encode(buffer.read()).decode())
            plt.close()

        countryData.append({
            'countryName': country,
            'plot_data_vaccinations': plot_data_vaccinations,
            'total_vaccinations':overall_total_vaccinations_by_country[country]
        })

    context = {
        'countryData':countryData,
        'available_years':available_years,
        'plot_data_vaccinations_combined':plot_data_vaccinations_combined
    }
    return render(request,'home/vaccinations.html',context)

def fetch_hospitalizations_data(request):
    csv_file_path= "static/data/covid-hospitalizations.csv"
    countries = COUNTRIES_HOSPITALIZATION
    total_hospitalizations_by_country_and_year,overall_total_hospitalizations_by_country,available_years = process_hospitalization_data(csv_file_path, countries)
    
    available_years.sort()
    
    plot_data_hospitalizations_combined = {}
    for year in available_years:
        # Plot for combined hospitalizations
        plt.figure(figsize=(8, 6))
        for country in countries:
            plt.plot(total_hospitalizations_by_country_and_year[country][year].keys(), total_hospitalizations_by_country_and_year[country][year].values(),label=country)
        plt.title('Monthly Hospitalizations')
        plt.xlabel('Month')
        plt.ylabel('Total Hospitalizations')
        plt.xticks(rotation=45, ha='right')

        buffer = io.BytesIO()
        plt.legend(countries)
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        plot_data_hospitalizations_combined[year] = urllib.parse.quote(base64.b64encode(buffer.read()).decode())
        plt.close()

    countryData = []
    for country in countries:
        # Plot for total hospitalizations
        plot_data_hospitalizations = {}
        for year in available_years:
            plt.figure(figsize=(8, 6))
            plt.bar(total_hospitalizations_by_country_and_year[country][year].keys(), total_hospitalizations_by_country_and_year[country][year].values())
            plt.title(f'Monthly Hospitalizations - {country}')
            plt.xlabel('Month')
            plt.ylabel('Total Hospitalizations')
            plt.xticks(rotation=45, ha='right')

            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            plot_data_hospitalizations[year] = urllib.parse.quote(base64.b64encode(buffer.read()).decode())
            plt.close()

        countryData.append({
            'countryName': country,
            'plot_data_hospitalizations': plot_data_hospitalizations,
            'total_hospitalizations':overall_total_hospitalizations_by_country[country]
        })

    context = {
        'countryData':countryData,
        'available_years':available_years,
        'plot_data_hospitalizations_combined':plot_data_hospitalizations_combined
    }
    return render(request,'home/hospitalizations.html',context)

def redirect_plot_page(request):
    plot_type = request.GET.get('plot_type')
    if plot_type:
        # Determine the URL based on the selected plot
        if plot_type == 'vaccinations':
            redirect_url = reverse('vaccinations')  # name of vaccinations URL
        elif plot_type == 'deaths':
            redirect_url = reverse('deaths')  # name of deaths URL
        elif plot_type == 'cases':
            redirect_url = reverse('cases')  # name o cases URL
        elif plot_type == 'hospitalizations':
            redirect_url = reverse('hospitalizations')  # Use the name of hospitalizations URL

        return redirect(redirect_url)

    return render(request, 'homepage.html')



