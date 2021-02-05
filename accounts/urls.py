from django.urls import path

from . import views
from .views import *

app_name = 'accountsapp'

urlpatterns = [
    path('home/signup/', signup, name='signup'),
    path('home/login/', login, name='login'),
    path('home/logout/', logout, name='logout'),
    path('home/', home, name='home'),
]
