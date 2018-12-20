from django.urls import path, include

from . import views

urlpatterns = [
    path(
        '',
        views.landing,
        name='lootlists-landing'
    ),
    path(
        'list/',
        views.ListListView.as_view(),
        name="lootlists-dashboard"
    ),
    path(
        'list/new/',
        views.ListCreateView.as_view(),
        name='lootlists-new_list'
    ),
    path(
        'list/<int:pk>/',
        views.ListDetailView.as_view(),
        name='lootlists-list'
    ),
    path(
        'list/<int:pk>/update/',
        views.ListUpdateView.as_view(),
        name='lootlists-update_list'
    ),
    path(
        'list/<int:pk>/delete/',
        views.ListDeleteView.as_view(),
        name='lootlists-delete_list'
    ),
    path(
        'list/<int:list_id>/item/new/',
        views.ItemCreateView.as_view(),
        name='lootlists-new_item'
    ),
    path(
        'list/<int:list_id>/item/<int:pk>/update/',
        views.ItemUpdateView.as_view(),
        name='lootlists-update_item'
    )
]
