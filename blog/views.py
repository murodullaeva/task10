from django.shortcuts import render, redirect, get_object_or_404
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





def friends_detail(request,pk):
    friend = get_object_or_404(Friend,pk=pk)
    context = {'friend': friend}
    return render(request,'friends_detail.html',context)


def friend_update(request,pk):
    friend = get_object_or_404(Friend,pk=pk)
    if request.method == 'POST':
        form = AcharyaFriendForm(request.POST,instance=friend)
        if form.is_valid():
            form.save()
            return redirect('friend')
        else:
            form = AcharyaFriendForm(instance=friend)
        context = {
            "form": form,
        }
        return render(request,'friends_update.html')



def friend_delete(request,pk):
    friend = get_object_or_404(Friend,pk=pk)
    friend.delete()
    return render(request,'friends_delete.html')