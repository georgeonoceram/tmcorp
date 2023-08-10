# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from tmglobal.models.corporativo import Clientes, Fornecedores
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    # return render(request, "tmglobal/pages/hlogin.html")
    return render(request, "registration/login.html")


@login_required
def hcorp(requests):
    return render(requests, "tmglobal/pages/hcorp.html")


@login_required
def vw_corpfor(request):
    vfornece = Fornecedores.objects.all()
    return render(
        request, "tmglobal/pages/glbcadfornecedor.html", {"vfornece": vfornece}
    )


class ClientListViewBase(LoginRequiredMixin, ListView):
    model = Clientes
    context_object_name = "vwclientes"
    ordering = ["-cliente_pk"]
    template_name = "tmglobal/pages/glbcorp_hp.html"
    paginate_by = 3

    def get_queryset(self):
        txt_nomecli = self.request.GET.get("nm_com_cli")
        if txt_nomecli:
            vclientes = Clientes.objects.filter(nm_com_cli__icontains=txt_nomecli)
        else:
            vclientes = Clientes.objects.all()
        return vclientes


def test(requests):
    return render(requests, "tmglobal/pages/glbcorp_hp.html")
