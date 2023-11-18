from django.urls import path
from . import views
urlpatterns = [ 
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("design/", views.design, name="design"),
    path("contact/", views.contact, name="contact"),
]
