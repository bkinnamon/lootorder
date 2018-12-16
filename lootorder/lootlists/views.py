from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request.user)
            return redirect('lootlists-dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', { 'form': form })



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
