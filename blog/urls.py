from .views import home
from django.urls import path
from .views import  friend ,AcharyaFriend ,friends_detail , friend_update , friend_delete
urlpatterns = [
    path('',home,name='home'),
    path('friend/', friend,name='friend'),
    path('my_friends/', AcharyaFriend, name='AcharyaFriend'),
    path('friends_detail/<int:pk>/', friends_detail, name='friends_detail'),
    path('friend_update/', friend_update, name='friend_update'),
    path('friend_delete/', friend_delete, name='friend_delete')

]