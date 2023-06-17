from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db import models

from item.models import Category, Item


from .forms import SignupForm

# Create your views here.

def index(request):
    all_items = Item.objects.filter(is_sold=False)
    paginator = Paginator(all_items, 10)
    page_number = request.GET.get('page')
    items = paginator.get_page(page_number)
    categories = Category.objects.all()
    popular_categories = Category.objects.annotate(item_count=models.Count('items')).order_by('-item_count')[:5]
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
        'popular_categories': popular_categories,
    })

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