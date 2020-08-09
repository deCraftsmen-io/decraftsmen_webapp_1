from django.urls import path

from . import views

app_name = 'TestApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('hello/<name>/', views.hello, name='hello'),
]
