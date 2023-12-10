from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm
from .models import News
from .forms import NewsForm


def form(request):
    name = request.POST.get('name', 'Unverifed')

    return render(request, 'form.html')

def postuser(request):
    name = request.POST.get('name', 'Unverifed')
    age = request.POST.get('age', 1)
    langs = request.POST.getlist('languages', ['python'])

    return HttpResponse(f'<div>Name: {name} Age: {age}</div>'
                        f'<div>Languages: {langs}</div>')

def index(request):
    userform = UserForm()
    return render(request, 'index.html', {'form': userform})

def appointment(request):
    name = request.POST.get('name', 'Unverifed')
    second_name = request.POST.get('second_name', 'Unverifed')
    phone_number = request.POST.get('phone_number', 'Unverifed')
    service = request.POST.get('service', 'Unverifed')
    car_info = request.POST.get('car_info', 'Unverifed')
    return HttpResponse(f'<div>Name: {name}<br> Second name: {second_name}</div><br>'
                        f'<div>Phone number: {phone_number}<br> Service name: {service}</div><br>'
                        f'<div>Test: {car_info}</div><br>')

def order(request):
    name = request.POST.get('name', 'Unverifed')
    second_name = request.POST.get('second_name', 'Unverifed')
    email = request.POST.get('email', 'Unverifed')
    country = request.POST.get('country', 'Unverifed')
    city = request.POST.get('city', 'Unverifed')
    street = request.POST.get('street', 'Unverifed')
    home_num = request.POST.get('home_num', 'Unverifed')
    home = request.POST.get('home', 'Unverifed')

    return HttpResponse(f'<div>{name} {second_name}, проверьте адрес доставки:<br>'
                        f'Страна: {country}<br>Город: {city}<br>Улица:{street}, {home_num}<br>Квартира: {home}</div><br>')


def news_list(request):
    news = News.objects.all()
    return render(request, 'news_list.html', {'news': news})

def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm()
    return render(request, 'add_news.html', {'form': form})