from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.landing, name='lootlists-landing'),
    path('list/', views.ListListView.as_view(), name="lootlists-dashboard"),
    path('list/new/', views.ListCreateView.as_view(), name='lootlists-new_list'),
    path('list/<int:pk>/', views.ListDetailView.as_view(), name='lootlists-list'),
]
