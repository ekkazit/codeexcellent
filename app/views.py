from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {
        'menu': 'index',
    })


def service(request):
    return render(request, 'service/index.html', {
        'menu': 'service',
    })


def teacher(request):
    return render(request, 'teacher/index.html', {
        'menu': 'teacher',
    })


def customer(request):
    return render(request, 'customer/index.html', {
        'menu': 'customer',
    })


def contact(request):
    return render(request, 'contact/index.html', {
        'menu': 'contact',
    })
