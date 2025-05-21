from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction, IntegrityError

def index(request):
    return render(request, 'index.html')