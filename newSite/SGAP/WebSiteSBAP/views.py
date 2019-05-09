from django.shortcuts import render

# Create your views here.
def funcio(request):
    return render(request, 'template/Site/Funcio.html', {})
