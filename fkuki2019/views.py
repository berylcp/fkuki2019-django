from django.shortcuts import render, get_object_or_404
from fkuki2019.models import Materi, Nilai, Jadwal
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/akun/login/')
def materi(request):
    materis = Materi.objects.all()

    p = Paginator(materis, 5)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    context = {'materis': page}
    return render(request, 'fkuki2019/materi.html', context)

@login_required(login_url='/akun/login/')
def materi_detail(request, slug=None):
    materi = get_object_or_404(Materi, slug=slug)
    return render(request, 'fkuki2019/materi-detail.html', {'materi': materi})

@login_required(login_url='/akun/login/')
def nilai(request):
    nilais = Nilai.objects.all()
    return render(request, 'fkuki2019/nilai.html', {'nilais': nilais})

@login_required(login_url='/akun/login/')
def jadwal(request):
    jadwals = Jadwal.objects.all()
    return render(request, 'fkuki2019/jadwal.html', {'jadwals': jadwals})