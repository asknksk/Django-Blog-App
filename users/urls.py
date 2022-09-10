from django.urls import path

from users.views import profile, register, user_login, user_logout

urlpatterns = [
    path('', register, name="register"),
    path('logout/', user_logout, name="user_logout"),
    path('login/', user_login, name="user_login"),
    path('profile/', profile, name = 'profile'),
]
