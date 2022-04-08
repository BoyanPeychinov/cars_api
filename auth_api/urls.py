from django.urls import path

from auth_api.views import RegisterView, LoginView, ListUsers, GetEditDeleteUser

urlpatterns = [
    path('', ListUsers.as_view(), name='list-users'),
    path('<int:pk>', GetEditDeleteUser.as_view(), name='list-users'),
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
]