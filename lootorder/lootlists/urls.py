from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.landing, name='lootlists-landing'),
    path('dashboard/', views.dashboard, name='lootlists-dashboard'),
    path('list/new', views.ListCreateView.as_view(), name='lootlists-new_list')
    # path('list/', views.new_list, name='lootlists-new_list')
]
