from django.shortcuts import render, redirect
from django.urls import reverse_lazy
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
from .models import LootList
from .forms import LootListForm


def landing(request):
    if request.user.is_authenticated:
        return redirect('lootlists-dashboard')
    form = UserRegisterForm()
    return render(request, 'lootlists/landing.html', { 'form': form })


class ListListView(LoginRequiredMixin, ListView):
    model = LootList
    template_name = 'lootlists/dashboard.html'
    context_object_name = 'lists'

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
