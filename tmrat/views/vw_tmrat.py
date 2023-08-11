from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from tmrat.models import RelAtTec
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin


class ForneceListViewBase(LoginRequiredMixin, ListView):
    model = RelAtTec
    context_object_name = "vwrat"
    ordering = ["-rat_pk"]
    template_name = "tmglobal/pages/glbcorp_hp.html"
    paginate_by = 3

    def get_queryset(self):
        txt_ratcli = self.request.GET.get("cod_cli")
        if txt_ratcli:
            vrat = RelAtTec.objects.filter(cod_cli__icontains=txt_ratcli)
        else:
            vrat = RelAtTec.objects.all()
        return vrat
