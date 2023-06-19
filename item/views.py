from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewItemForm, EditItemForm
from .models import Item, Category, Status

def browse(request):
    items = Item.objects.filter(is_sold=False)
    query = request.GET.get('query', '')
    max_price = request.GET.get('max_price')
    min_price = request.GET.get('min_price')
    categories = Category.objects.all()

    if max_price:
        items = items.filter(price__lte=max_price)  # Replace 'price' with the name of your new query input

    if min_price:
        items = items.filter(price__gte=min_price)  # Replace 'price' with the name of your new query input

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query) | Q(category__name__icontains=query) | Q(status__status__icontains=query))


    return render(request, 'item/browse.html', {
        'items': items,
        'query': query,
        'max_price': max_price,  # Include the new variable in the dictionary
        'min_price': min_price,
        'categories': categories,

    })

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:5]
    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Ny inlägg'
    })

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    return redirect('dashboard:index')

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Redigera inlägg'
    })