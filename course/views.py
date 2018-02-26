from django.shortcuts import render, get_object_or_404


def index(request):
    return render(request, 'course/index.html', {
        'menu': 'course',
    })


def detail(request, slug):
    return render(request, 'course/detail.html', {
        'menu': 'course',
    })
