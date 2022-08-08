from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("search_result/", views.search_result, name="search_result"),
    path("<int:id>/", views.flight_detail, name="flight_detail"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
