from django.shortcuts import render


def index(request):
    return render(request, 'blog/index.html', {
        'menu': 'blog',
    })


def detail(request, slug):
    return render(request, 'blog/detail.html', {
        'menu': 'blog',
    })
