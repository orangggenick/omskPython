from random import random, randint

from django.shortcuts import render
from AdminOmsk.models import Article, Person, Place


def home(request):
    randomPerson = randint(1, int(Person.objects.count()))
    randomPlace = randint(1, int(Place.objects.count()))
    return render(request, 'AdminOmsk/home.html', {'articles':Article.objects.all(), 'person':Person.objects.get(id=randomPerson), 'place':Place.objects.get(id=randomPlace)})