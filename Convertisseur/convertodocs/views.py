from altair import Detail
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "convertodocs/index.html")


def Acceuil(request):
    return render(request, "convertodocs/Acceuil.html")


def Contact(request):
    return render(request, "convertodocs/contact.html")


def jobdetails(request):
    return render(request, "convertodocs/job-details.html")


def joblistings(request):
    return render(request, "convertodocs/job-listings.html")


def about(request):
    return render(request, "convertodocs/about.html")