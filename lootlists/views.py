from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from user.forms import UserRegisterForm
from .models import LootList, LootItem
from django.contrib.auth.models import User
from .forms import LootListForm
from dal import autocomplete


def landing(request):
    if request.user.is_authenticated:
        return redirect('lootlists-dashboard')
    form = UserRegisterForm()
    return render(request, 'lootlists/landing.html', { 'form': form })


class ListListView(LoginRequiredMixin, ListView):
    template_name = 'lootlists/dashboard.html'
    context_object_name = 'lists'

    def get_queryset(self):
        return self.request.user.lootlist_set.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Dashboard'
        context['guest_lists'] = self.request.user.guest_lists.all()
        return context


class ListCreateView(LoginRequiredMixin, CreateView):
    model = LootList
    form_class = LootListForm

    def form_valid(self, form):
        messages.success(self.request, 'New list created')
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'New List'
        return context


class ListDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = LootList

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name
        return context

    def test_func(self):
        list = self.get_object()
        return list.owner == self.request.user or self.request.user in list.guests.all()


class ListUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = LootList
    form_class = LootListForm

    def form_valid(self, form):
        messages.success(self.request, 'List updated')
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        list = self.get_object()
        return list.owner == self.request.user


class ListDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = LootList
    success_url = reverse_lazy('lootlists-dashboard')

    def test_func(self):
        list = self.get_object()
        return list.owner == self.request.user


class ItemCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = LootItem
    fields = ['name']

    def dispatch(self, request, *args, **kwargs):
        self.lootlist = get_object_or_404(LootList, id=self.kwargs['list_id'])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lootlist'] = self.lootlist
        context['is_new'] = True
        return context

    def form_valid(self, form):
        form.instance.list = self.lootlist
        return super().form_valid(form)

    def test_func(self):
        return self.lootlist.owner == self.request.user


class ItemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = LootItem
    fields = ['name']

    def dispatch(self, request, *args, **kwargs):
        self.lootlist = get_object_or_404(LootList, id=self.kwargs['list_id'])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lootlist'] = self.lootlist
        context['is_new'] = False
        return context

    def form_valid(self, form):
        form.instance.list = self.lootlist
        return super().form_valid(form)

    def test_func(self):
        return self.lootlist.owner == self.request.user


def toggle_item(request, list_id, pk):
    item = get_object_or_404(LootItem, id=pk)

    if item.taken is None:
        messages.success(request, f'You have claimed {item.name}.')
        item.taken = request.user
        item.save()
    elif item.taken == request.user:
        messages.success(request, f'You have unclaimed {item.name}.')
        item.taken = None
        item.save()
    else:
        messages.error(request, f'You cannot unclaim {item.name}.')

    return redirect('lootlists-list', pk=list_id)


class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = LootItem

    def get_success_url(self):
        return reverse('lootlists-list', kwargs={'pk': self.kwargs['list_id']})

    def test_func(self):
        return self.get_object().list.owner == self.request.user


class UserAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return User.objects.none()
        results = User.objects.all()
        if self.q:
            results = results.filter(username__icontains=self.q)
        return results
