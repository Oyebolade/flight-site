from multiprocessing import context
from unittest import result
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

# Create your views here.
from flight.models import Flight

def home(request):
    #if "Departure" in request.GET:
   #     departure = request.GET["Departure"]
    #    flights = Flight.objects.filter(departure__country__icontains=departure)
   # elif "Destination" in request.GET:
   #      destination = request.GET["Destination"]
   #      flights = Flight.objects.filter(destination__country__icontains=destination)
   # elif "Departure_date" in request.GET:
   #      departure_date = request.GET["Departure_date"]
    #     flights = Flight.objects.filter(departure_date__country__icontains=departure_date)
   # elif "Destination_date" in request.GET:
   #      destination_date = request.GET["Destination_date"]
   #      flights = Flight.objects.filter(destination_date__country__icontains=destination_date)
   # else:
    #    flights = Flight.objects.all()
    
   # context = {
   #    "queryset": flights
  #  }
   
    return render(request, "flight/home.html")


def about(request):
    return render(request, "flight/about.html")


def contact(request):
    return render(request, "flight/contact.html")


def search_result(request):
    print(request)
    if "Departure" in request.GET:
        departure = request.GET["Departure"]
        flights = Flight.objects.filter(departure__country__icontains=departure)
    elif "Destination" in request.GET:
         destination = request.GET["Destination"]
         flights = Flight.objects.filter(destination__country__icontains=destination)
    elif "Departure_date" in request.GET:
         departure_date = request.GET["Departure_date"]
         flights = Flight.objects.filter(departure_date__country__icontains=departure_date)
    elif "Destination_date" in request.GET:
         destination_date = request.GET["Destination_date"]
         flights = Flight.objects.filter(destination_date__country__icontains=destination_date)
    else:
        flights = Flight.objects.all()
    
    context = {
        "queryset": flights
    }
   
    return render(request, "flight/search_result.html", context)
   # flights = Flight.objects.all()
   # if request.method =="GET":
   #  departure = request.GET.get("Departure")
   #  destination = request.GET.get("Destination")
   #  departure_date = request.GET.get("Departure_date")
    # destination_date = request.GET.get("Destination_date")
    
   #  if departure != "" and departure is not None:
   #    flights =flights.filter(departure__country__icontains=departure)
   # elif destination != "" and destination is not None:
   #    flights =flights.filter(destination__country__icontains=destination)
   # elif departure_date != "" and departure_date is not None:
  #     flights =flights.filter(departure_date__country__icontains=departure_date)
   # elif destination_date != "" and destination_date is not None:
   #    flights =flights.filter(destination_date__country__icontains=destination_date)
   
   # context = {
   #     "queryset": flights
   # }
    
   # return render(request, "flight/search_result.html")


def flight_detail(request,id):
    context = {"flight": get_object_or_404(Flight,id=id)}
    return render(request, "flight/flight_detail.html", context)
