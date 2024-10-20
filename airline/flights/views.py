from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Flight,Passenger
from django.urls import reverse
# Create your views here.
def indexa(request):
     return render(request,"flights/index.html",{
         "flights": Flight.objects.all()
     })
def flight(request,flight_id):
    flight = Flight.objects.get(pk=flight_id)
    return render(request,"flights/flight.html",{
        "flight":flight,
        "passengers":flight.passengers.all(),
        "non_passengers":Passenger.objects.exclude(flight=flight).all()
    })
def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flight.add(flight)
        return HttpResponseRedirect(reverse("flight",args = (flight.id,)))
def accueil(request):
    return render(request, 'accueil.html')