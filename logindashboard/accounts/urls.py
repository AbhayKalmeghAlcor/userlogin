from django.urls import path, include
from .import views
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    path('login/', views.login, name='login')
]