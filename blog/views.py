from django.shortcuts import render, redirect
from .models import Friend
from .forms import AcharyaFriendForm

def home(request):
    return render(request, 'home.html')

def friend(request):
    friends = Friend.objects.all()
    return render(request, 'dostlar.html', {'friends': friends})

def AcharyaFriend(request):
    if request.method == 'POST':
        form = AcharyaFriendForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('friend')
    else:
        form = AcharyaFriendForm()

    return render(request, 'my_friends.html', {'form': form})