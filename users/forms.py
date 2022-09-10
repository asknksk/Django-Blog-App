from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from users.models import UserProfile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        # fields = __all__
        exclude = ('user',)  # hangi field harici istiyorsam user haricindekilerin tümünü getirir
        #tek elemanlı tupple kullandığımız için sonuna , koyduk