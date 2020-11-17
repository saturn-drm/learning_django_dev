from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        return redirect('/movie/index')
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def logout(request):
    messages.add_message(request, messages.SUCCESS, 'Logged out!')
    return redirect('/movie/index')