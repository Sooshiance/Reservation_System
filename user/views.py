from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages

from user.models import Profile
from user.forms import RegisterUser, LoginUser


def logoutUser(request):
    auth.logout(request)
    messages.info(request, '')
    return redirect('booking:home')


def loginUser(request):
    if request.user.is_authenticated:
        return redirect("")
    elif request.method == "POST":
        form = LoginUser(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = auth.authenticate(request=request, username=username, password=password)
            if user is not None:
                auth.login(request)
                return redirect("")
            else:
                messages.error(request, "user not found")
                return redirect("user:login")
        else:
            messages.error(request, "Form is not valid")
            return redirect("user:login")
    else:
        form = LoginUser()
    return render(request, "user/login.html", {'form':form})


def registerUser(request):
    if request.user.is_authenticated:
        messages.warning(request, '')
        return redirect("booking:home")
    elif request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user = User.objects.create_user(email=email, username=username, password=password1,first_name=first_name,
                                            last_name=last_name)
            user.set_password(password1)
            user.is_active = True
            user.save()
            messages.success(request, '')
            return redirect('user:login')
        else:
            messages.error(request, f'{form.errors}')
            return redirect('user:register')
    else:
        form = RegisterUser()
    return render(request, "user/register.html", {'form': form})


def userProfile(request):
    if request.user.is_authenticated:
        user = request.user
        p = Profile.objects.get(user=user)
        return render(request, "user/profile.html", {'profile':p})
    else:
        messages.info(request, "")
        return redirect("user:login")
