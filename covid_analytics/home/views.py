from django.shortcuts import render
import matplotlib.pyplot as plt
import io
import urllib
import base64

# Create your views here.
def home(request):
    background_image_url='images/covidbanner.jpg' 
    return render(request,'home/home.html',{'background_image_url': background_image_url})


def dashboard(request):

    categories = ['Category A', 'Category B', 'Category C']
    values = [20, 14, 23]

    # plt.figure(figsize=(8, 6))
    # plt.bar(categories, values)
    # plt.title('Bar Chart')
    # plt.xlabel('Categories')
    # plt.ylabel('Values')
    
    # buffer = io.BytesIO()
    # plt.savefig(buffer, format='png')
    # buffer.seek(0)
    # plot_data = urllib.parse.quote(base64.b64encode(buffer.read()).decode())

    countryData=[
        {
            'countryName' : 'India',
            'total_deaths': 1000000,
            'total_vaccinated': 20000,
            'total_hospitalizations':10000,
        },
        {
            'countryName' : 'New Zealand',
            'total_deaths': 2000000,
            'total_vaccinated': 30000,
            'total_hospitalizations':20000,
        },
        {
            'countryName' : 'Pakistan',
            'total_deaths': 3000000,
            'total_vaccinated': 40000,
            'total_hospitalizations':30000,
        },
        {
            'countryName' : 'America',
            'total_deaths': 4000000,
            'total_vaccinated': 50000,
            'total_hospitalizations':50000,
        }
    ]


    for country in countryData:
        # Create a new plot for each country
        plt.figure(figsize=(8, 6))
        plt.bar(categories, values)
        plt.title(f'Bar Chart - {country["countryName"]}')
        plt.xlabel('Categories')
        plt.ylabel('Values')

        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        country['plot_data'] = urllib.parse.quote(base64.b64encode(buffer.read()).decode())


    context = {
        'countryData':countryData
    }
    return render(request,'home/dashboard.html',context)