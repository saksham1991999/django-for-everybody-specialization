
from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('owner', views.owner, name='owner'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]