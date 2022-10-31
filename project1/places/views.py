from django.shortcuts import redirect, render
from .models import Place
from comments.models import Review
from django.core.paginator import Paginator
from django.db import IntegrityError


def places_list(request):
    template_name = '../templates/place.html'
    places_list = Place.objects.filter(is_pamyatnik=False)
    places_list_count = Place.objects.filter(is_pamyatnik=False).count()
    dost_qt = Place.objects.filter(is_pamyatnik=False).count()
    pam_qt = Place.objects.filter(is_pamyatnik=True).count()

    context = {
        'places': places_list,
        'dost_qt': dost_qt,
        'pam_qt': pam_qt,
        'count': places_list_count,
    }
    if request.GET:
        title = request.GET['title']
        context['places'] = Place.objects.filter(is_pamyatnik=False).filter(title__icontains=title)
        context['count'] = Place.objects.filter(is_pamyatnik=False).filter(title__icontains=title).count()

    return render(request, template_name, context)


def place_detail(request, id):
    template_name = '../templates/Showplace.html'
    place = Place.objects.get(pk=id)
    reviews = Review.objects.filter(place=place)
    reviews_qt = Review.objects.filter(place=place).count()

    context = {
        'place': place,
        'reviews': reviews,
        'review_qt': reviews_qt,
    }

    if request.method == 'POST':
        user = request.user
        text = request.POST['text']
        try:
            Review.objects.create(user=user, text=text, place=place)
           
        except IntegrityError:
            return render(request, template_name, context)       

    return render(request, template_name, context)


def pam_places_list(request):
    template_name = '../templates/place.html'
    places_list = Place.objects.filter(is_pamyatnik=True)
    places_list_count = Place.objects.filter(is_pamyatnik=True).count()
    dost_qt = Place.objects.filter(is_pamyatnik=False).count()
    pam_qt = Place.objects.filter(is_pamyatnik=True).count()


    context = {
        'places': places_list,
        'dost_qt': dost_qt,
        'pam_qt': pam_qt,
        'count': places_list_count,
    }

    if request.GET:
        title = request.GET['title']
        context['places'] = Place.objects.filter(is_pamyatnik=True).filter(title__icontains=title)
        context['count'] = Place.objects.filter(is_pamyatnik=True).filter(title__icontains=title).count()

    return render(request, template_name, context)
