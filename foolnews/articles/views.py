from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'articles/index.html', context)

def detail(request):
    context = {}
    return render(request, 'articles/detail.html', context)