# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from tmglobal.models.corporativo import Clientes, Fornecedores


def home(request):
    # return render(request, "tmglobal/pages/hlogin.html")
    return render(request, "registration/login.html")


@login_required
def hcorp(requests):
    return render(requests, "tmglobal/pages/hcorp.html")


@login_required
def vw_corpcli(request):
    vclientes = Clientes.objects.all()
    return render(
        request, "tmglobal/pages/glbcadcliente.html", {"vclientes": vclientes}
    )


@login_required
def vw_corpfor(request):
    vfornece = Fornecedores.objects.all()
    return render(
        request, "tmglobal/pages/glbcadfornecedor.html", {"vfornece": vfornece}
    )
