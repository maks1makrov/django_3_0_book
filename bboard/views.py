from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from bboard.models import Bd


def index(request):
    template = loader.get_template('bboard/index.html')
    bbs = Bd.objects.order_by('-published')
    context = {'bbs': bbs}
    return HttpResponse(template.render(context, request))
