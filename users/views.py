from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import  login, logout
from django.contrib.auth.decorators import login_required
from users.forms import UserProfileForm, UserRegisterForm


def register(request):
    form = UserRegisterForm()
    form_profile = UserProfileForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        form_profile = UserProfileForm(request.POST, request.FILES)
        if form.is_valid() and form_profile.is_valid():
            user = form.save()
            # username = form.cleaned_data.get('username')
            profile = form_profile.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            return redirect('home')
    
    context = {
        'form_profile' : form_profile,
        'form' : form,
    }
    # form = UserRegisterForm()
    return render(request, 'users/registration/register.html', context)

def user_logout(request):
    logout(request)
    return redirect('home')

def user_login(request):
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('home')
    
    return render(request, 'users/registration/login.html', {'form' : form})

@login_required
def profile(request):
    return render(request, 'users/registration/profile.html')