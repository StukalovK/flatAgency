from django.shortcuts import render, redirect
from .forms import OfferForm, DistrictForm
from .models import Offer, District, Picture, Category
from django.core.paginator import Paginator


def offer_list(request):
    all_offers = Offer.objects.all()
    paginator = Paginator(all_offers, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    numbers = [x for x in range(1, page_obj.paginator.num_pages+1)]
    return render(request, 'catalog/offer-list.html', context={
        'page_obj': page_obj,
        'numbers': numbers,
    })



def create(request):
    if request.method == 'GET':
        return render(request, 'catalog/create.html', context={
            'form': OfferForm()
        })
    elif request.method == 'POST':
        ready_form = OfferForm(request.POST, request.FILES)
        ready_form.save()
        return redirect('/catalog/offer-list')


def details(request, offer_id):
        single_offer = Offer.objects.get(id=offer_id)
        pictures = Picture.objects.filter(offer_id=offer_id)
        category = Category.objects.get(id=single_offer.category_id)
        return render(request, 'catalog/details.html', context={
            'offer': single_offer,
            'pictures': pictures,
            'category': category,
    })


def delete(request, offer_id):
    del_offer = Offer.objects.get(id=offer_id)
    if request.method == 'GET':
        return render(request, 'catalog/delete.html', context={
            'del_offer': del_offer
        })

    elif request.method == 'POST':
        del_offer.delete()
        return redirect('/catalog/offer-list')


def district_list(request):
    return render(request, 'catalog/district-list.html', context={
        'all_districs': District.objects.all()
    })


def add_district(request):
    if request.method == 'GET':
        return render(request, 'catalog/add-district.html', context={
            'form': DistrictForm()
        })
    elif request.method == 'POST':
        ready_form = DistrictForm(request.POST, request.FILES)
        ready_form.save()
        return redirect('/catalog/district-list')


def delete_district(request, district_id):
    del_district = District.objects.get(id=district_id)
    if request.method == 'GET':
        return render(request, 'catalog/delete-district.html', context={
            'del_district': del_district
        })

    elif request.method == 'POST':
        del_district.delete()
        return redirect('/catalog/district-list')


