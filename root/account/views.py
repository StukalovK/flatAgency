from django.shortcuts import render


def signin(request):
    return render(request, 'account/signin.html')


def signout(request):
    return render(request, 'account/signout.html')


def signup(request):
    return render(request, 'account/signup.html')

