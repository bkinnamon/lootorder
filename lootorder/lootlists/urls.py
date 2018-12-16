from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.dashboard, name='lootlists-dashboard'),
    path('user/', include('django.contrib.auth.urls')),
    path('user/signup/', views.signup, name='signup'),
]
