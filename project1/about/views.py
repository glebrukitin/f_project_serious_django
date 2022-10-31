from django.views.generic import ListView
from django.shortcuts import render
from .models import About, GaleryPhoto
from places.models import Place


def history(request):
    template_name = '../templates/history.html'
    about = About.objects.all().first()

    context = {
        'about': about,
    }

    return render(request, template_name, context)


class galery(ListView):
    paginate_by = 9
    model = GaleryPhoto
    template_name = '../templates/galery.html'


def index(request):
    template_name = '../templates/Index.html'
    about = About.objects.all().first()
    places_list = Place.objects.filter(is_pamyatnik=False).filter()[:5]
    dost_qt = Place.objects.filter(is_pamyatnik=False).count()
    monuments_list = Place.objects.filter(is_pamyatnik=False).filter()[:8]
    pam_qt = Place.objects.filter(is_pamyatnik=True).count()

    context = {
        'about': about,
        'monuments': monuments_list,
        'places': places_list,
        'dost_qt': dost_qt,
        'pam_qt': pam_qt,
    }

    return render(request, template_name, context)


def index_1(request):
    template_name = '../templates/Index_1.html'
    about = About.objects.all().first()
    places_list = Place.objects.filter(is_pamyatnik=True).filter()[:5]
    dost_qt = Place.objects.filter(is_pamyatnik=False).count()
    monuments_list = Place.objects.filter(is_pamyatnik=True).filter()[:8]
    pam_qt = Place.objects.filter(is_pamyatnik=True).count()

    context = {
        'about': about,
        'monuments': monuments_list,
        'places': places_list,
        'dost_qt': dost_qt,
        'pam_qt': pam_qt,
    }

    return render(request, template_name, context)