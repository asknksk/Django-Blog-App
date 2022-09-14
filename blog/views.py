from django.shortcuts import render, redirect

from blog.forms import BlogForm
from .models import Post
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (LoginRequiredMixin)
from django.views.generic import (CreateView)

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-publish_date')
    template_name = 'blog/index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

# @login_required
# def blog_create(request):
#     form = BlogForm()
#     if request.method == 'POST':
#         form = BlogForm(request.POST)
#         if form.is_valid():
#             blog = form.save(commit=False)
#             blog.user = request.user
#             blog.save()
#             return redirect('home')
#     context = {'form': form}
#     return render(request, 'blog/blog_create.html', context)

class PostCreateView(LoginRequiredMixin, CreateView): # make sure you add your mixins to the left. They should be inherited first, in other words
    model = Post
    fields = ('title', 'content', 'image', 'status', 'slug')
    success_url = '/'

    # we are getting a "NOT NULL constraint failed: blog_post.author_id" after posting a blog post which
    # means that the post needs an author and django by default cannot know who the author is. Therefore,
    # we'll need to override the form_valid method and set the author before saving it
    def form_valid(self, form):     
        form.instance.author = self.request.user
        return super().form_valid(form)