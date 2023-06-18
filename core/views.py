from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db import models


import random


from item.models import Category, Item


from .forms import SignupForm

# Create your views here.

def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:index')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })


def index(request):
    all_items = Item.objects.filter(is_sold=False)
    paginator = Paginator(all_items, 10)
    page_number = request.GET.get('page')
    items = paginator.get_page(page_number)
    categories = Category.objects.all()
    popular_categories = Category.objects.annotate(item_count=models.Count('items')).order_by('-item_count')[:5]
            

    slogans= [
    "Upptäck gömda skatter på dina fingertoppar!",
    "Din allt-i-ett-butik för unika fynd!",
    "Där jakten på fynd blir till äventyr!",
    "Släpp loss din inre skattjägare!",
    "Upplås en värld av vintagecharm och udda nöjen!",
    "Från dammiga vindar till din dörrsteg - loppismagi!",
    "Omfamna glädjen i secondhand med oss!",
    "Bläddra. Pruta. Bliss.",
    "Utgräv eklektiska juveler till oslagbara priser!",
    "Där begagnat blir förstahandsvalet!",
    "Kurerade kuriositeter för varje smak och budget!",
    "Återupptäck konsten att skrota med lätthet!",
    "Byt, pruta och hitta din perfekta bit!",
    "Stig in i en förtrollande värld av loppisfynd!",
    "Vintagevibbar och antikförtjusning väntar!",
    "Din ingång till vintage-chic och retro-återupplivning!",
    "Hållbar stil börjar här - Grönt är skönt, loppis är toppen!",
    "Omfamna det förflutna, omfamna fynden!",
    "Lås upp historierna bakom varje föremål!",
    "Där de bästa fynden hittar dig!",
    "Utforska skatter och fynd med oss!",
    "Låt oss ta dig på en fyndresa!",
    "Hitta det oväntade hos oss på loppmarknaden!",
    "Fynda unika prylar till oslagbara priser!",
    "Ge ditt hem en touch av retro och vintage!",
    "Loppisfynd som passar din stil och plånbok!",
    "Skapa ditt eget hem med charmiga secondhand-fynd!",
    "Få nostalgiska vibbar på vår loppisplats!",
    "Upptäck en värld av begagnade skatter!",
    "Få mer för mindre på vår virtuella loppis!",
    "Hitta dolda pärlor i varje hörn av vår marknad!",
    "Gör miljömedvetna val genom att handla secondhand!",
    "En skattkista av möjligheter väntar på dig!",
    "Låt oss göra din fyndresa rolig och spännande!",
    "Skapa ett unikt hem med våra loppisfynd!",
    "Utforska en värld av vintage och retro hos oss!",
    "Gör historiska fynd utan att lämna ditt hem!",
    "Låt loppisfynden berätta din egen historia!",
    "Fånga stilen från förr med våra fantastiska fynd!",
    "Gör varje dag till en loppisdag hos oss!"
]
    
    random_slogan = random.choice(slogans)



    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
        'popular_categories': popular_categories,
        'random_slogan': random_slogan,
    })