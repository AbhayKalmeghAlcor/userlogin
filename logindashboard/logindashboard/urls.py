from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', include('loginauth.urls')),
    path('', include('accounts.urls')),
    path('', include('home.urls'))
]
