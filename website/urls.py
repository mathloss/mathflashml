from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add.html', views.add, name="add"),
    path('add0100.html', views.add0100, name="add0100"),
    path('add01000.html', views.add01000, name="add01000"),
    path('subtract.html', views.subtract, name="subtract"),
    path('subtract0100.html', views.subtract0100, name="subtract0100"),
    path('subtract01000.html', views.subtract01000, name="subtract01000"),
    path('mutliply.html', views.multiply, name="multiply"),
    path('mutliply0510.html', views.multiply0510, name="multiply0510"),    
    path('about.html', views.about, name="about"),

]
