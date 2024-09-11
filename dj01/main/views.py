from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница о нас'
    }
    return render(request, 'main/index.html', data)


def data(request):
    data = {
        'title': 'Немножко информации о немецких овчарках'
    }
    return render(request, 'main/data.html', data)


def test(request):
    data = {
        'title': 'Проверим Ваши знания о породе'
    }
    return render(request, 'main/test.html', data)


def about_page(request):
    data = {
        'title': 'Немножко информации обо мне любимом'
    }
    return render(request, 'main/about.html', data)
