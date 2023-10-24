from django.shortcuts import render

# Create your views here.
def home(request):
    background_image_url='images/covidbanner.jpg' 
    return render(request,'home/home.html',{'background_image_url': background_image_url})


def dashboard(request):
    return render(request,'home/dashboard.html')