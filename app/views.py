from django.shortcuts import render

# Create your views here.

def about(request):
    template = 'about.html'
    return render(request,template)