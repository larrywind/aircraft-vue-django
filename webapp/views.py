import logging

from django.shortcuts import render

logger = logging.getLogger("root")


def home_page(request):
    return render(request, "index.html")
