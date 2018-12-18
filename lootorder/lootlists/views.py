from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user.forms import UserRegisterForm


def landing(request):
    if request.user.is_authenticated:
        return redirect(request, 'lootlists-dashboard')
    form = UserRegisterForm()
    return render(request, 'lootlists/landing.html', { 'form': form })


@login_required
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
