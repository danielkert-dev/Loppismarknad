from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewItemForm, EditItemForm
from .models import Item, Category, CategoryGroup, Status

from django.core.mail import send_mail
from django.contrib.auth.models import User

def browse(request):
    query = request.GET.get('query', '')
    max_price = request.GET.get('max_price')
    min_price = request.GET.get('min_price')
    created_from = request.GET.get('created_from', '')
    created_to = request.GET.get('created_to', '')
    category_id = request.GET.get('category')
    status_id = request.GET.get('status')

    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category_id=category_id)

    if status_id:
        items = items.filter(status_id=status_id)

    if max_price:
        items = items.filter(price__lte=max_price)

    if min_price:
        items = items.filter(price__gte=min_price)

    if created_from:
        items = items.filter(created_at__gte=created_from)

    if created_to:
        items = items.filter(created_at__lte=created_to)

    if query:
        keywords = query.split()
        query_filter = Q()

        for keyword in keywords:
            query_filter |= Q(name__icontains=keyword) | Q(category__name__icontains=keyword) | Q(status__status__icontains=keyword)

        items = items.filter(query_filter)

    items = items[:20]  # Apply slicing after all filters

    categories_group = CategoryGroup.objects.all()
    categories = Category.objects.all()
    status = Status.objects.all()

    return render(request, 'item/browse.html', {
        'items': items,
        'query': query,
        'max_price': max_price,
        'min_price': min_price,
        'created_from': created_from,
        'created_to': created_to,
        'categories_group': categories_group,
        'categories': categories,
        'category_id': category_id,
        'status': status,
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
            item.user = request.user
            item.save()

            recipients = User.objects.filter(emailnotification__email=True)
            if recipients.exists():
                recipient_emails = recipients.values_list('email', flat=True)
                recipient_names = recipients.values_list('first_name', flat=True)

                item_name = item.name  # Get the item name
                item_price = item.price  # Get the item price
                item_id = item.id # Get the item id

                send_mail(
                    'En ny inlägg har skickats!',
                    f'https://loppismarknad.com/.\n\nNamn: {item_name}\nPris: {item_price}\n\n{", ".join(recipient_names)}',
                    'danielkertdev@gmail.com',  # Replace with your email address
                    recipient_emails,
                    fail_silently=True,
                )

            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm(request=request)

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