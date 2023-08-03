from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import SignupForm, ItemForm, CommentForm, ProfileForm, MessaForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Item, Like, Comment, Notification, Profile, Messa
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core.paginator import Paginator


category_mappings = {
    '肉':'meat',
    '魚':'fish',
    '野菜':'vegetable',
    '果物':'fruit',
    'お菓子':'snack',
    '飲み物':'drink'
}

def top(request):
    items = Item.objects.all()
    user = request.user
    context = {
        'items': items,
        'user': user
    }
    return render(request, 'top.html', context)

def signup(request):
    if request.method == 'POST':
       form = SignupForm(request.POST)
       if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            password = make_password(form.cleaned_data.get('password'))

            user = CustomUser.objects.create(username=username, email=email, password=password)
            Profile.objects.create(user=user, name=username, image='item_images/default_image.jpeg',
                                   content='これはデフォルトのプロフィールです。好みに応じて編集してください')
            login(request, user)
            return redirect('profile', user_id=user.id)

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


def profile(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    items = user.items.all()
    profile = get_object_or_404(Profile, user=user)

    context = {
        'user' : user,
        'profile': profile,
        'items': items
    }
    return render(request,'profile.html', context)

@login_required
def profile_edit(request):
    if request.method == 'POST':
      form = ProfileForm(request.POST, request.FILES)
      user = request.user
      user_id = user.id
      if form.is_valid():
        profile_data = form.cleaned_data
        profile = Profile.objects.filter(user=user).first()
        if profile:
            profile.name = profile_data['name']
            profile.image = profile_data['image']
            profile.content = profile_data['content']
            profile.save()
        else:
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
        return redirect('profile', user_id=user_id)
    else:
        form = ProfileForm()
    return render(request,'profile_edit.html', {'form' : form})


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
  self_id = item_id
  item = get_object_or_404(Item, pk=item_id)
  user = item.user
  profile = get_object_or_404(Profile, user=user)
  items = Item.objects.exclude(id=self_id)[:4]
  comments = Comment.objects.filter(item_id=item_id)
  context = {
    'item' : item,
    'comments' : comments,
    'items' : items,
    'profile' : profile
  }
  return render(request,'food_information.html', context)



@login_required
def get_like_status(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    is_liked = Like.objects.filter(user=request.user, item=item).exists()
    response_data = {
        'is_liked': is_liked,
        }
    return JsonResponse(response_data)


def like_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    like, created = Like.objects.get_or_create(user=request.user, item=item, is_liked=True)

    if created:
        item.like_count += 1
        is_liked = True
        notification_content = f"{request.user.username}さんがアイテム「{item.name}」にいいねしました"
        Notification.objects.create(user=item.user, item=item, content=notification_content)

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


@login_required
def comment_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    user = request.user

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            comment = Comment.objects.create(user=user, item=item, text=text)
            notification_content = f"{user.username}さんがアイテム「{item.name}」にコメントしました"
            Notification.objects.create(user=item.user, item=item, content=notification_content)
            comment_data = {
                'text': comment.text,
                'user': comment.user.username,
            }
            return JsonResponse({'success': True, 'comment': comment_data})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = CommentForm()

    return render(request, 'food_information.html', {'form': form})


def notification(request):
    user = request.user
    notifications = Notification.objects.filter(user=user).order_by('-timestamp')
    Notification.objects.filter(user=user, read=False).update(read=True)

    paginator = Paginator(notifications, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'notification.html', {'page_obj':page_obj})

def check_new_notifications(request):
    user = request.user
    has_new_notifications = Notification.objects.filter(user=user, read=False).exists()

    response_data = {'hasNewNotification': has_new_notifications}
    return JsonResponse(response_data)

def search(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')
        search_category = category_mappings.get(query, query)
        results = Item.objects.filter(category=search_category)
    else:
        results = None
    return  render(request, 'search.html', {'results': results})


def search_category(request):
    return render(request, 'search_category.html')

def want(request, item_id):
    item =  get_object_or_404(Item, pk=item_id)
    user1 = item.user.profile
    messages = Messa.objects.filter(item=item)

    context = {
        'item' : item,
        'user1' : user1,
        'messages' : messages
    }
    return render(request, 'want.html', context)

def message(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    user = request.user

    if request.method == 'POST':
        form = MessaForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['content']
            reply_to = form.cleaned_data['reply_to']


            if reply_to:
                reply_to_id = reply_to.id
                original_message = Messa.objects.get(id=reply_to_id)
                receiver = original_message.sender
                message = Messa.objects.create(sender=user, receiver=receiver, item=item, content=message, reply_to=original_message)
                notification_content = f"{item.user}さんがあなたのメッセージ「{original_message.content}」に対して返信しました"
                Notification.objects.create(user=receiver, item=item, content=notification_content)

            else:
                message = Messa.objects.create(sender=user, receiver=item.user, item=item, content=message)

            if item.user != user:
                notification_content = f"{user.username}さんがあなたの食品「{item.name}」に対してメッセージを送信しました"
                Notification.objects.create(user=item.user, item=item, content=notification_content)

            formatted_timestamp = message.timestamp.strftime("%B %d, %Y, %I:%M %p")
            sender = None
            message_data = {
                'message': message.content,
                'user' : user.profile.name,
                'image' : user.profile.image.url,
                'sender' : message.sender_id,
                'timestamp' : formatted_timestamp
            }
            return JsonResponse({'success': True, 'message': message_data})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = CommentForm()
    return render(request, 'want.html')
