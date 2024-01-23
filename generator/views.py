import datetime
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
import random
from django.contrib.auth.forms import UserCreationForm
from generator.models import Passwords
from django.contrib.auth import login, authenticate


# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def about(request):
    return render(request, 'generator/about.html')


def password(request):
    characters = list('qwertyuiopasdfghjklzxcvbnm')

    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    lenght = int(request.GET.get('lenght', 12))
    thepassword = ''

    for x in range(lenght):
        thepassword += random.choice(characters)

    password_to_models = Passwords(password=thepassword, created_at = datetime)
    password_to_models.save()

    return render(request, 'generator/password.html', {'password': thepassword})


def pass_list(request):
    context = {
        "passwords_list": Passwords.objects.all()
    }

    return render(request, 'generator/created_pass.html', context=context)


# def registration (request: HttpRequest) -> HttpResponse:
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('/')
#     else:
#         form = UserCreationForm()
#     return render(request, 'generator/signup.html', {'form': form})
