import json
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Subscribe


def home(request):
    return render(request, "landingPage/home.html", {})


def subscribe(request):
    if request.method == "GET":
        return HttpResponse(status=405)

    breakpoint()
    name = request.POST.get("name")
    email = request.POST.get("email")
    try:
        s = Subscribe.objects.get(email=email)
    except ObjectDoesNotExist:
        s = Subscribe(email=email)
    s.name = name
    s.save()

    return HttpResponse(status=200)
