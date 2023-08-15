from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    tanit = Tanit.objects.all()
    card = Card.objects.all()
    return render(request, 'index.html',
                  {
                      'tanit': tanit,
                      'card': card,
                  })


def about(request):
    context = dict()
    templates = 'about.html'
    return render(request, templates, context)
