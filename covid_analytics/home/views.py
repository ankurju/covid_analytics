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
    total_deaths = 15000
    total_vaccinated = 100000

    categories = ['Category A', 'Category B', 'Category C']
    values = [20, 14, 23]

    plt.figure(figsize=(8, 6))
    plt.bar(categories, values)
    plt.title('Bar Chart')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data = urllib.parse.quote(base64.b64encode(buffer.read()).decode())



    context = {
        'total_deaths': total_deaths,
        'total_vaccinated': total_vaccinated,
        'plot_data':plot_data
    }
    return render(request,'home/dashboard.html',context)