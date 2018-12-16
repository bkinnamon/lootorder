from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def dashboard(request):
    context = {
        'title': 'Dashboard',
        'lists': [
            { 'name': 'One', 'description': 'The first list.' },
            { 'name': 'Two', 'description': 'The second list.' },
            { 'name': 'Three', 'description': 'The third list.' },
        ]
    }
    return render(request, 'lootlists/dashboard.html', context)
