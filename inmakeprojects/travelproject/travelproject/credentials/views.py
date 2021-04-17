from django.contrib import auth
from django.contrib.auth.models import User
from django.core.mail import message
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            message.info(request, "invalid")
            return redirect('login')

    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                message.info(request, "username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                message.info(request, "email taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name, email=email)
                user.save()
                print("user created")
                return redirect('login')
        else:
            print("password not matched")
            message.info(request, "password not matching")
            return redirect('register')
        return redirect('/')
    return render(request, "registration.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
