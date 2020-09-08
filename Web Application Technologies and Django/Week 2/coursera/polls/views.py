from django.shortcuts import render, HttpResponse

# Create your views here.
def HomeView(request):
    return HttpResponse("Hello, world. 78573683 is the polls index.")