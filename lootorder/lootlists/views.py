from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user.forms import UserRegisterForm
from .models import LootList


def landing(request):
    if request.user.is_authenticated:
        return redirect(request, 'lootlists-dashboard')
    form = UserRegisterForm()
    return render(request, 'lootlists/landing.html', { 'form': form })


@login_required
def dashboard(request):
    lists = LootList.objects.filter(user=request.user)
    context = {
        'title': 'Dashboard',
        'lists': lists
    }
    return render(request, 'lootlists/dashboard.html', context)
