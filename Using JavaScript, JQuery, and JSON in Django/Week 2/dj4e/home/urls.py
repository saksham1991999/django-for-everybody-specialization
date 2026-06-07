from django.urls import path
from . import views

#defining url patterns
urlpatterns = [
    path('', views.HomeView.as_view()),
]
