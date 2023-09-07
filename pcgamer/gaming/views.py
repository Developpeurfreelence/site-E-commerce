from django.shortcuts import render
from django.http import HttpResponse
from .models import Game
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect



# Create your views here.

from .forms import SearchForm


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("index")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()

    return render(request, "name.html", {"form": form})


def index(request):

    gamers = Game.objects.all()
    
    item_name = request.GET.get('item-name')
    if item_name !='' and item_name is not None:
        gamers = Game.objects.filter(name__icontains=item_name # Search title
        # Search description
        )

    paginator = Paginator(gamers, 4)
    page = request.GET.get("page")
    gamers = paginator.get_page(page)
   


    
    return render(request, "gaming/index.html", {"gamers": gamers})

def details(request, product_id):
 gamers = Game.objects.get(id=product_id)
 return render(request, "gaming/details.html", {"gamers": gamers})

def checkout(request):
    gamers = Game.objects.all()
    return render(request, "gaming/checkout.html", {"gamers": gamers})
  
 


