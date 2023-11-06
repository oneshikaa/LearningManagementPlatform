from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeView.as_view(),name='index'),
    # path('',views.index,name='index'),
    path('register.html/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('view_profile/<str:username>/', views.view_profile, name='view_profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
]