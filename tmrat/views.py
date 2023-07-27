from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def htmrat(request):
    return render(request, "tmrat/pages/htmrat.html")
