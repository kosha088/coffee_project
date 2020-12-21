from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from auth_user.forms import UserForm


def login_page(request):
    if request.user.is_authenticated:
        return redirect('main')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_auth = authenticate(request, username=username, password=password)
        if user_auth:
            login(request, user_auth)
            return redirect('main')
    return render(request,'auth_user/login.html')

def register_page(request):
    if request.user.is_authenticated:
        return redirect('main')
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserForm
    content = {
        'form': form,
    }
    return render(request, 'auth_user/register.html', content)

def logout_page(request):
    logout(request)
    return redirect('main')



