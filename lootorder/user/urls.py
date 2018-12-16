from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.login, name='user-login'),
    path('signup/', views.signup, name='user-signup'),
]
