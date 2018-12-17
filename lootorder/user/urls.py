from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.login_view, name='user-login'),
    path('signup/', views.signup, name='user-signup'),
    path('logout/', views.logout_view, name='user-logout'),
]
