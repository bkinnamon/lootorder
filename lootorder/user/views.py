from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(requets.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request.user)
            return redirect('lootlists-dashboard')
    else:
        form = UserCreationForm()
    context = {
        'title': 'Signup',
        'form': form,
    }
    return render(request, 'user/forms.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(requets.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request.user)
            return redirect('lootlists-dashboard')
    else:
        form = AuthenticationForm()
    context = {
        'title': 'Login',
        'form': form,
    }
    return render(request, 'user/forms.html', context)
