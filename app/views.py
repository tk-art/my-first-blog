from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from .forms import SignupForm, ItemForm

from django.contrib.auth.hashers import make_password
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST





# Create your views here.

def top(request):
  return render(request, 'top.html')

def signup(request):
    if request.method == 'POST':
       form = SignupForm(request.POST)
       if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            password = make_password(form.cleaned_data.get('password'))

            user = CustomUser.objects.create(username=username, email=email, password=password)
            login(request, user)
            return redirect('profile')

    else:
      form = SignupForm()
    return render(request, 'signup.html', {'form': form})



def login_form(request):
    error_message = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('top')
        else:
            error_message = 'ユーザーネームかパスワードが違いますね、もう一度お試しを'

    return render(request, 'login.html', {'error_message': error_message})


@require_POST
def logout_view(request):
    logout(request)
    return redirect('top')



@login_required
def profile(request):
  return render(request,'profile.html', { 'user': request.user })

@login_required
def register_view(request):
    if request.method == 'POST':
      form = ItemForm(request.POST, request.FILES)
      if form.is_valid():
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        print(item)
        return redirect('food_information')
    else:
        form = ItemForm()

    return render(request,'register.html', { 'user': request.user })

def food_information(request):
  return render(request,'food_information.html', { 'uesr': request.user })
