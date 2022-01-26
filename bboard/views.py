from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from bboard.models import Bd


def index(request):
    bbs = Bd.objects.order_by('-published')
    return render(request, 'bboard/index.html', {'bbs': bbs})
