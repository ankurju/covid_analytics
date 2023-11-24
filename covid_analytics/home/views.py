from django.shortcuts import render
from django.http import HttpResponse
import matplotlib.pyplot as plt
import io
import urllib
import base64
from home.test.test import process_data

# avoid some of the issues associated with running Matplotlib in a non-GUI environment.
import matplotlib
matplotlib.use('Agg')



# Create your views here.
def home(request):
    background_image_url='images/covidbanner.jpg' 
    return render(request,'home/home.html',{'background_image_url': background_image_url})


def dashboard(request):
    csv_file_path = "static/data/full_data_deaths.csv"
    countries = ['India', 'Pakistan', 'Australia', 'New Zealand']

    total_cases_by_country_and_year, total_deaths_by_country_and_year, available_years = process_data(
        csv_file_path, countries
    )

    countryData = []
    

    for country in countries:
        # Plot for total deaths
        plot_data_deaths = {}
        plot_data_cases = {}
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
            'total_deaths': 0,
            'total_vaccinated': 0,
            'total_hospitalizations': 0,
            'plot_data_deaths': plot_data_deaths,
            'plot_data_cases': plot_data_cases
        })

    # print(countryData[0]['plot_data_deaths'])

    context = {
        'countryData':countryData,
        'available_years':available_years
    }
    return render(request,'home/dashboard.html',context)