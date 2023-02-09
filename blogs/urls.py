from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='Home'),
    path('login',views.login,name='Login'),
    path('signup',views.signup,name='Signup'),
    path('blogs',views.blog,name='blogs'),
    path('profile/<str:name>',views.profile,name='profile')
]
