from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
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
from .forms import LootListForm


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
        return context


class ListCreateView(LoginRequiredMixin, CreateView):
    model = LootList
    fields = ['name', 'description']

    def form_valid(self, form):
        messages.success(self.request, 'New list created')
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'New List'
        return context


class ListDetailView(LoginRequiredMixin, DetailView):
    model = LootList

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name
        return context


class ListUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = LootList
    fields = ['name', 'description']

    def form_valid(self, form):
        messages.success(self.request, 'List updated')
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        list = self.get_object()
        return list.user == self.request.user


class ListDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = LootList
    success_url = reverse_lazy('lootlists-dashboard')

    def test_func(self):
        list = self.get_object()
        return list.user == self.request.user


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
        return self.lootlist.user == self.request.user


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
        return self.lootlist.user == self.request.user


def toggle_item(request, list_id, pk):
    item = get_object_or_404(LootItem, id=pk)
    item.taken = not item.taken
    item.save()
    return redirect('lootlists-list', pk=list_id)


class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = LootItem

    def get_success_url(self):
        return reverse('lootlists-list', kwargs={'pk': self.kwargs['list_id']})

    def test_func(self):
        return self.get_object().list.user == self.request.user
