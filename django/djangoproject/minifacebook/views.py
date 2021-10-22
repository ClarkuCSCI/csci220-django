from django.shortcuts import render

from .models import Profile

def index(request):
    context = {"profiles": Profile.objects.all()}
    return render(request, "index.html", context)
