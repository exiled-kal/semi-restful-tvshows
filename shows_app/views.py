from django.shortcuts import render, redirect
from .models import Show
from datetime import datetime, time, timezone
from time import gmtime, strftime

# Create your views here.


def index(request):
    context = {
        "shows":Show.objects.all()
    }
    return render(request, 'AllShows.html', context)

# 1. # GET /shows/new ------ 'show' was 'shows'


def AddNewShow(request):  # GET /shows/new

    return render(request, "AddNewShow.html")

# 2. # POST /shows/create


def CreateNewShow(request):  
    show = Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], description=request.POST['description'])
                              
    return redirect(f"/shows/{show.id}")

# 3. GET shows/id


def TvShow(request, id):
    context = {
        'show': Show.objects.get(id=id)
    }
    return render(request, "TVShow.html", context)

# 4 GET /shows ------ 'show' was 'shows'


def AllShows(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, "AllShows.html", context)

# 5 GET /shows/<id>


def EditShow(request, id):
    context = {
        'show': Show.objects.get(id=id)
    }
    return render(request, "EditShow.html", context)

# 6 POST shows/<id>/update


def UpdateShow(request, id):
    show = Show.objects.get(id=id)
    show.title = request.POST['title']
    show.network = request.POST['network']
    show.release_date = request.POST['release_date']
    show.description = request.POST['description']
    show.save
    return redirect(f"/shows/{show.id}/edit")

# 7 POST shows/<id>/destroy
def DeleteShow(request, id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect(f"/shows")
