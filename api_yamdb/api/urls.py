from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (UserViewSet, get_token, register)

v1_router = DefaultRouter()
v1_router.register(r'users', UserViewSet)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/auth/signup/', register, name='register'),
    path('v1/auth/token/', get_token, name='token')

]