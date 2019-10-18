from django.shortcuts import render


def index(request, main):
    return render(request, 'index.html', {'research': main.research, 'time': main.time})
