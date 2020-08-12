from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone
from urllib.parse import urlencode
from django.urls import reverse


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    if sort == 'названию':
        phones = Phone.objects.order_by('name')
    elif sort == 'начиная с дешевых':
        phones = Phone.objects.order_by('price')
    elif sort == 'начиная с дорогих':
        phones = Phone.objects.order_by('-price')
    else:
        phones = Phone.objects.all()
    context = {
        'phones': phones,
        'sort': {
            'названию': f"{reverse('catalog')}?{urlencode({'sort': 'названию'})}",
            'начиная с дешевых': f"{reverse('catalog')}?{urlencode({'sort': 'начиная с дешевых'})}",
            'начиная с дорогих': f"{reverse('catalog')}?{urlencode({'sort': 'начиная с дорогих'})}",
            }.items()
        }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones = get_object_or_404(Phone, slug=slug)
    context = {'phones': phones}
    return render(request, template, context)

def home(request):
    return redirect('catalog')
