from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import register_user, public_view, protected_view

urlpatterns = [
    path("register/",register_user),
    path('login/',obtain_auth_token),
    path('public/',public_view),
    path('protected/',protected_view),
]
