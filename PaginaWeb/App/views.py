from django.shortcuts import render

# Create your views here.
def Inicio(request):

    return render(request, 'App/index.html')

def Nosotros(request):
    
    return render(request, 'App/about.html')

def Services(request):
    
    return render(request, 'App/services.html')

def Contact(request):
    
    return render(request, 'App/contact.html')

