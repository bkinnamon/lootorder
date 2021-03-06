from django.urls import path, include
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    path(
        'favicon.ico',
        RedirectView.as_view(
            url=staticfiles_storage.url('favicon.ico'),
            permanent=False
        ),
        name='favicon'
    ),
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
    ),
    path(
        'list/<int:list_id>/item/<int:pk>/toggle/',
        views.toggle_item,
        name='lootlists-toggle_item'
    ),
    path(
        'list/<int:list_id>/item/<int:pk>/delete/',
        views.ItemDeleteView.as_view(),
        name='lootlists-delete_item'
    ),
    path(
        'usersearch/',
        views.UserAutocomplete.as_view(),
        name='lootlists-user_search'
    ),
]
