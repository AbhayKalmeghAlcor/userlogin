from django.urls import path, include
from django.contrib import admin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    path('user/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('admin/', admin.site.urls),
    path('api/login/', include('loginauth.urls')),
    path('', include('accounts.urls')),
    path('', include('home.urls')),
    path('noti/', include('notifications.urls'))
]

admin.site.site_title = "High5 Admin"
admin.site.site_header = "High5 Cloud Admin"
admin.site.index_title = "High5 Cloud Admin Panal"
