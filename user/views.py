from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, LoginForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import logout, login, authenticate
# from django.urls import reverse
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Registration successful for {username}. Continue to Log in')
            return redirect('user-login')
    else:
        form = CreateUserForm()
    context = {
        'form':form
    }
    return render(request, 'user/register.html', context)


def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("dashboard-index")
            else:
                messages.error(request, "Invalid username or password")
    
    else:
        form = LoginForm()

    return render(request, 'user/login.html', {'form': form})




def logout_view(request):
    logout(request)
    return render(request, 'user/logout.html')

def profile(request):
    return render(request, 'user/profile.html')

def profileUpdate(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('user-profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'user_form':user_form,
        'profile_form':profile_form,
    }
    return render(request, 'user/profileUpdate.html', context)