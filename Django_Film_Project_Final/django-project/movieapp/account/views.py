from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return redirect('movies:movie_list')  # Zaten giriş yapmışsa film listesine yönlendir
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Başarıyla giriş yaptınız!')
            return redirect('movies:movie_list')  # Film listesine yönlendir
        else:
            messages.error(request, 'Kullanıcı adı veya şifre hatalı!')
    
    return render(request, 'account/login.html')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('movies:movie_list')  # Zaten giriş yapmışsa film listesine yönlendir
        
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Hesabınız başarıyla oluşturuldu!')
            return redirect('movies:movie_list')  # Film listesine yönlendir
    else:
        form = UserCreationForm()
    return render(request, 'account/register.html', {'form': form})

@login_required
def profile_view(request):
    return render(request, 'account/profile.html')
