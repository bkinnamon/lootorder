from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'Account created')
            return redirect('lootlists-dashboard')
    else:
        form = UserCreationForm()
    context = {
        'title': 'Signup',
        'submit': 'Signup',
        'form': form,
    }
    return render(request, 'user/forms.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('lootlists-dashboard')
        else:
            messages.error(request, 'Login error')
    form = AuthenticationForm()
    context = {
        'title': 'Login',
        'submit': 'Login',
        'form': form,
    }
    return render(request, 'user/forms.html', context)


def logout_view(request):
    logout(request)
    messages.success(request, 'Logout successful')
    return redirect('lootlists-dashboard')
