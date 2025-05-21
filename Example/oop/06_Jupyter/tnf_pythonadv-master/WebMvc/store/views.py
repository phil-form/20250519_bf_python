from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.template import loader
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction, IntegrityError

from .forms import ComposerForm

from .models import Composer

def index(request):
    composers = Composer.objects.all()
    paginator = Paginator(composers, 5)
    page = request.GET.get('page')
    max_page = paginator.num_pages
    try:
        composer_list = paginator.page(page)
        current_page = int(page)
    except PageNotAnInteger:
        composer_list = paginator.page(1)
        current_page = 1
    except EmptyPage:
        composer_list = paginator.page(paginator.num_pages)
        current_page = paginator.num_pages
    
    pages = []
    for i in range(int(current_page), max_page +1):
        pages.append(i)
    
    context = {
        'composers': composer_list,
        'pages': pages
    }
    return render(request, 'store/index.html', context=context)

@transaction.atomic
def insertComposer(request):
    context = {}
    if request.method == "POST":
        form = ComposerForm(request.POST)
        if form.is_valid():
            composer = form.save(commit=False)
            composer.save()
            
            return redirect('/')
        else:
            context['errors'] = form.errors.items()
    return render(request, 'store/composerForm.html', context=context)

@transaction.atomic
def composerDetails(request, id):
    composer = get_object_or_404(Composer, pk=id)
    context = {}
    context['composer'] = composer
    
    return render(request, 'store/details.html', context=context)

@transaction.atomic
def composerDetails2(request):
    id = request.GET.get('query')
    composer = get_object_or_404(Composer, pk=id)
    context = {}
    context['composer'] = composer
    
    return render(request, 'store/details.html', context=context)