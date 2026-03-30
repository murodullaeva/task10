from django.urls import path
from .views import home
from django.urls import path
from .views import AcharyaFriend , friend
urlpatterns = [
    path('',home,name='home'),
    path('my_friends/', AcharyaFriend, name='AcharyaFriend'),
    path('friend/', friend,name='Friend'),

]