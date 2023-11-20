"""
URL configuration for django2FAEmail project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path, include
from django_otp.forms import OTPAuthenticationForm
from two_factor.urls import urlpatterns as tf_urls

from myapp.views import (
    ExampleSecretView, HomeView, RegistrationView, RegistrationCompleteView, DownloadView
)

from two_factor.admin import AdminSiteOTPRequired

# admin.site.__class__ = AdminSiteOTPRequired


urlpatterns = [
    # path('accounts/login/', LoginView.as_view(authentication_form=OTPAuthenticationForm)),
    # path('admin/', admin.site.urls),
    path('', include(tf_urls)),
    path('', HomeView.as_view(), name='home'),
    path(
        'account/logout/', LogoutView.as_view(), name='logout',
    ),
    path('secret/', ExampleSecretView.as_view(), name='secret'),
    path('download/', DownloadView.as_view(), name='download'),

    path(
        'account/register/',
        RegistrationView.as_view(),
        name='registration',
    ),
    path(
        'account/register/done/',
        RegistrationCompleteView.as_view(),
        name='registration_complete',
    ),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

