from django.shortcuts import render, get_object_or_404
from . models import Record


def main(request):
    return render(request, 'core/index.html', {});


