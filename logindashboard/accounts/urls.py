from django.urls import path, include
from . import views

urlpatterns = [
    path('account/user/', views.Accountuser.as_view(), name='account-user'),
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', views.registerUser, name='register'),
    path('logout/', views.LogoutAPIView.as_view(), name="logout"),
    path('profile/', views.getUserProfile, name="users-profile"),
    path('profile/update/', views.updateUserProfile, name="user-profile-update"),
    path('getUsers/', views.getUsers, name="users"),
    path('<str:pk>/', views.getUserById, name='user'),
    path('update/<str:pk>/', views.updateUser, name='user-update'),
    path('delete/<str:pk>/', views.deleteUser, name='user-delete'),
    path('request/password/', views.RequestPasswordResetEmail.as_view(),
         name="request-reset-email"),
    path('passwordreset/<uidb64>/<token>/',
         views.PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('passwordreset/complete', views.SetNewPasswordAPIView.as_view(),
         name='password-reset-complete')

]
