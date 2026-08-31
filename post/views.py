from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import Post
from .forms import PostForm


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'form.html'
    success_url = reverse_lazy('xabarlar')  


class PostListView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    ordering = ['-id']  