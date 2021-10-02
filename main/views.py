from django.shortcuts import render
from fkuki2019.models import Materi
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/akun/login/')
def index(request):
    return render(request, 'main/index.html')

@login_required(login_url='/akun/login/')
def cari(request):
    q = request.GET.get('q', None)
    items = ''
    if q == None or q == "":
        materis = Materi.objects.all()
    elif q is not None:
        materis = Materi.objects.filter(Q(title__contains=q) | Q(description__contains=q))

    return render(request, 'main/cari.html', {'materis': materis})