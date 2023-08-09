from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from tmrat.models import RelAtTec


@login_required
def htmrat(request):
    vrelattec = RelAtTec.objects.all().order_by("rat_pk")
    return render(request, "tmrat/pages/htmrat.html", {"vrelattec": vrelattec})
