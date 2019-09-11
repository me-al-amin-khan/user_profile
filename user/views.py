from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserForm, UserProfileForm
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'user/index.html')


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm()
        profile_form = UserProfileForm()

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()


    profile_info = {
        'registered': registered,
        'user_form': user_form,
        'profile_form': profile_form,
    }


    return render(request, 'user/registration.html', profile_info)



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
        else:
            print('Wrong login data provided!')
    return render(request, 'user/login.html')

@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect(reverse('index'))
