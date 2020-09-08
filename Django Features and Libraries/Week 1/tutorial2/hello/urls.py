from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name='polls'

urlpatterns = [
    path('', TemplateView.as_view(template_name='main.html')),
    path('cookie', views.cookie),
    path('hello/', views.sessfun),
]