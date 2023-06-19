from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewItemForm, EditItemForm
from .models import Item, Category

def browse(request):
    items = Item.objects.filter(is_sold=False)
    query = request.GET.get('query', '')
    max_price = request.GET.get('max_price')
    min_price = request.GET.get('min_price')
    created_from = request.GET.get('created_from', '')
    created_to = request.GET.get('created_to', '')
    categories = Category.objects.all()

    if max_price:
        items = items.filter(price__lte=max_price)  # Replace 'price' with the name of your new query input

    if min_price:
        items = items.filter(price__gte=min_price)  # Replace 'price' with the name of your new query input

    if created_from:
        items = items.filter(created_at__gte=created_from)

    if created_to:
        items = items.filter(created_at__lte=created_to)

    if query:
        keywords = query.split()  # Split query into separate keywords
        query_filter = Q()  # Create an empty Q object

        for keyword in keywords:
            query_filter |= Q(name__icontains=keyword) | Q(category__name__icontains=keyword) | Q(status__status__icontains=query)

        items = items.filter(query_filter)

    return render(request, 'item/browse.html', {
        'items': items,
        'query': query,
        'max_price': max_price,  # Include the new variable in the dictionary
        'min_price': min_price,
        'categories': categories,
        'created_from': created_from,
        'created_to': created_to,

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