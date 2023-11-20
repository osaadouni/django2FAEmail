from django.urls import path

from .views import home, profile, CustomTwoFactoryLoginView


urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('profile/', profile, name='profile'),
    path('login/', CustomTwoFactoryLoginView.as_view(), name='login'),
]