from django.shortcuts import render, get_object_or_404


def index(request):
    return render(request, 'video/index.html', {
        'menu': 'video',
    })


def detail(request, slug):
    return render(request, 'video/detail.html', {
        'menu': 'video',
    })
