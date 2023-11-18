from django.shortcuts import render
import matplotlib.pyplot as plt
import io
import urllib
import base64
from home.test.test import process_data

# Create your views here.
def home(request):
    background_image_url='images/covidbanner.jpg' 
    return render(request,'home/home.html',{'background_image_url': background_image_url})


def dashboard(request):

    csv_file_path = "static/data/full_data_deaths.csv"
    countries_of_interest = ['India', 'Pakistan', 'Australia', 'New Zealand']

    total_deaths_by_country_and_month, total_cases_by_country_and_month , available_years = process_data(csv_file_path, countries_of_interest)

    countryData = []

    for country in countries_of_interest:
        # Plot for total deaths
        plt.figure(figsize=(8, 6))
        plt.bar(total_deaths_by_country_and_month[country].keys(), total_deaths_by_country_and_month[country].values())
        plt.title(f'Monthly Deaths - {country}')
        plt.xlabel('Month')
        plt.ylabel('Total Deaths')
        plt.xticks(rotation=45, ha='right')

        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        plot_data_deaths = urllib.parse.quote(base64.b64encode(buffer.read()).decode())

        # Plot for total cases
        plt.figure(figsize=(8, 6))
        plt.bar(total_cases_by_country_and_month[country].keys(), total_cases_by_country_and_month[country].values())
        plt.title(f'Monthly Cases - {country}')
        plt.xlabel('Month')
        plt.ylabel('Total Cases')
        plt.xticks(rotation=45, ha='right')

        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        plot_data_cases = urllib.parse.quote(base64.b64encode(buffer.read()).decode())

        countryData.append({
            'countryName': country,
            'total_deaths': 0,  
            'total_vaccinated': 0,  
            'total_hospitalizations': 0,  
            'plot_data_deaths': plot_data_deaths,
            'plot_data_cases': plot_data_cases,
        })

    context = {
        'countryData':countryData,
        'available_years':available_years
    }
    return render(request,'home/dashboard.html',context)