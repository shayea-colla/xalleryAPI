from django.views.generic.base import RedirectView
from django.shortcuts import render


def perms_view(request):
    template_name = "gallery/tmp.html"
    return render(request, template_name)
