from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from users.forms import UserRegisterForm

# Create your views here.
# def register(request):
#     form = UserCreationForm(request.POST or None)
#     # form = UserCreationForm()    # bu eski yöntem üstteki kısa olarak yapılabilir.
#     # if request.method == "POST":
#     #     form = UserCreationForm(request.POST or None)
#     if form.is_valid() :
#         form.save()
        
#         username = form.cleaned_data.get("username")
#         password = form.cleaned_data.get("password1")
       
#         user = authenticate(username=username, password=password)
#         login(request, user)

#         return redirect("home")

#     context = {
#         'form':form,
#     }

#     return render(request, 'users/registration/register.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/registration/register.html', {'form': form})