from django.urls import path 
from .views import (postListView,postDetailView,postCreateView,postUpdateView,postDeleteView,SignUpView)
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect



class CustomLoginView(auth_views.LoginView):
    template_name = 'login.html'
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('post_list')
        return super().dispatch(request, *args, **kwargs)

urlpatterns =[
    path('',postListView.as_view(),name='post_list'),
    path('post/<int:pk>/',postDetailView.as_view(),name='post_detail'),
    path('post/new/',postCreateView.as_view(),name='post_new'),
    path('post/<int:pk>/edit/',postUpdateView.as_view(),name='post_edit'),
    path('post/<int:pk>/delete/',postDeleteView.as_view(),name='post_delete'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),

]