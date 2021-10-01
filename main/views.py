from django.shortcuts import render
from fkuki2019.models import Materi
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.

@login_required(login_url='/akun/login/?next=/{{request.path}}')
def index(request):

    return render(request, 'main/index.html')

@login_required(login_url='/akun/login/?next=/{{request.path}}')
def cari(request):

    q = request.GET.get('q', None)
    items = ''
    if q is None or q is "":
        materis = Materi.objects.all()
    elif q is not None:
        materis = Materi.objects.filter(Q(judul__contains=q) | Q(deskripsi__contains=q))

    return render(request, 'main/cari.html', {'materis': materis})

@login_required(login_url='/akun/login/?next=/{{request.path}}')
def profil(request):

    return render(request, 'main/profil.html')