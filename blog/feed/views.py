from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.contrib.auth.models import User

from .models import Post
from .forms import PostModelForm


# def home(request):
#     context= {
#         'posts': Post.objects.all()
#         }
#     return render(request, 'feed/home.html', context)   

class PostListView(ListView):
    model = Post
    template_name = 'feed/home.html'
    context_object_name = 'posts'
    paginate_by = 5
    
    def get_queryset(self):
            return Post.objects.all().order_by('-created_at') 


class UserPostListView(ListView):
    model = Post
    template_name = 'feed/user_post_list.html'
    context_object_name = 'posts'
    paginate_by = 5
    
    def get_queryset(self):
        username = self.kwargs.get('username')
        user = get_object_or_404(User, username=username)
        return Post.objects.filter(user=user)


class PostDetailView(DetailView):
    model = Post
    

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostModelForm
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.pk})


class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostModelForm
    
    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.pk})

    def test_func(self) -> bool | None:
        post = self.get_object()
        
        if post.user == self.request.user:
            return True
        return False


class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self) -> bool | None:
        post = self.get_object()
        
        if post.user == self.request.user:
            return True
        return False
            
            

def about(request):
    return render(request, 'feed/about.html', context={})