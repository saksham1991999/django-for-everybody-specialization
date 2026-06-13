from django.shortcuts import render, HttpResponse

# Create your views here.
def HomeView(request):
    return HttpResponse("Hello, world. 5000ab6d is the polls index.")
