from django.urls import path 
from .views import (postListView,postDetailView,postCreateView,postUpdateView,postDeleteView,SignUpView)
from django.contrib.auth import views as auth_views


urlpatterns =[
    path('',postListView.as_view(),name='post_list'),
    path('post/<int:pk>/',postDetailView.as_view(),name='post_detail'),
    path('post/new/',postCreateView.as_view(),name='post_new'),
    path('post/<int:pk>/edit/',postUpdateView.as_view(),name='post_edit'),
    path('post/<int:pk>/delete/',postDeleteView.as_view(),name='post_delete'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='post_list'), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),

]