from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import SignupForm, ItemForm

from django.contrib.auth.hashers import make_password
from .models import CustomUser
from django.contrib.auth.decorators import login_required
#from django.views.decorators.http import require_POST
from .models import Item
from .models import Like
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

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
        return redirect('food_information', item_id=item.id)
    else:
        form = ItemForm()

    return render(request,'register.html', { 'user': request.user })



def food_information(request, item_id):
  item = get_object_or_404(Item, pk=item_id)
  return render(request,'food_information.html', { 'item': item, })



@login_required
def like_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    like, created = Like.objects.get_or_create(user=request.user, item=item)

    if created:
        item.like_count += 1
        is_liked = True
    else:
        like.delete()
        item.like_count -= 1 if item.like_count > 0 else 0
        is_liked = False

    item.save()
    response_data = {
      'is_liked': is_liked,
      'like_count': item.like_count
    }
    return JsonResponse(response_data)

def comment_item(request):
    item = get_object_or_404(Item, pk=item_id)

    if request.method == 'POST':
        # POSTリクエストの場合はコメントを作成または保存する処理を記述
        comment_text = request.POST.get('comment_text')
        comment = Comment(item=item, text=comment_text)
        comment.save()

        # コメントが正常に保存された場合、成功レスポンスを返す
        response_data = {'success': True}
        return JsonResponse(response_data)

    # POST以外のリクエストの場合はエラーレスポンスを返す
    response_data = {'error': 'Invalid request method'}
    return JsonResponse(response_data, status=400)
