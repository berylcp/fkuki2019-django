from django.shortcuts import render, get_object_or_404
from fkuki2019.models import Materi
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/akun/login/?next=/{{request.path}}')
def materi(request):

    materis = Materi.objects.all()

    return render(request, 'fkuki2019/materi.html', {'materis': materis})

@login_required(login_url='/akun/login/?next=/{{request.path}}')
def materi_detail(request, slug=None):
    
    materi = get_object_or_404(Materi, slug=slug)

    return render(request, 'fkuki2019/materi-detail.html', {'materi': materi})