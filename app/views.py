from django.shortcuts import render

# Create your views here.

def about(request):
    template = 'index.html'
    return render(request,template)