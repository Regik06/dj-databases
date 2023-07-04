from django.shortcuts import render
from .models import Phone


def show_catalog(request):
    template = 'catalog.html'
    sorting = request.GET.get('sort')
    if sorting == 'name':
        phones = Phone.objects.order_by(sorting)
    elif sorting == 'min_price':
        phones = Phone.objects.order_by('-price')
    elif sorting == 'max_price':
        phones = Phone.objects.order_by('price')
    else:
        phones = Phone.objects.all()

    context = {
        'phones': phones
    }

    return render(request, template, context)


def show_product(request, slug):
    phones = Phone.objects.filter(slug=slug)
    template = 'product.html'
    for phone in phones:
        context = {
            'phone': phone
        }
    return render(request, template, context)
