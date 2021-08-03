from django.urls import path

from . import views

app_name = 'clientModule'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:client_id>/', views.detail, name='detail'),
    path('/edit/<int:client_id>/', views.edit, name='edit'),
]