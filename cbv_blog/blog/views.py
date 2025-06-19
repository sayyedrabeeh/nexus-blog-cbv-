from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from.models import Post,Category
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView

# Create your views here.
class postListView(LoginRequiredMixin,ListView):
    login_url = 'login'
    model =Post
    template_name ='post_list.html'
    context_object_name='posts'
    paginate_by = 5 



class postDetailView(LoginRequiredMixin,DetailView):
    login_url = 'login'
    model=Post
    template_name = 'post_detail.html'

class postCreateView(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model=Post
    fields=['title','content',"category"]
    template_name = 'post_form.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()  
        return context
        
class postUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model=Post
    fields=['title','content','category']
    template_name='post_form.html'

class postDeleteView(LoginRequiredMixin,DeleteView):
    login_url = 'login'
    model=Post
    template_name='postconfirm_delete.html'
    success_url=reverse_lazy('post_list')


class SignUpView(FormView):
    template_name = 'signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('post_list')   

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
