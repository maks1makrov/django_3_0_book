from django.shortcuts import render
from django.http import HttpResponse

from bboard.models import Bd


def index(request):
    s = 'list of ads \r\n\r\n\r\n'
    for bd in Bd.objects.order_by('published'):
        s += bd.title + '\r\n' + bd.content + '\r\n\r\n'
    return HttpResponse(s, content_type='text/plain; charset=utf-8')
