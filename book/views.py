from django.shortcuts import render, get_object_or_404


def index(request):
    return render(request, 'book/index.html', {
        'menu': 'book',
    })


def detail(request, slug):
    return render(request, 'book/detail.html', {
        'menu': 'book',
    })
