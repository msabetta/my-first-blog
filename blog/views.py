from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views import View

from .models import Post
from .forms import PostForm

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from .serializers import PostSerializer 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import BaseFilterBackend
from rest_framework import filters
from django.views.generic import View, ListView

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

class BaseView(View):
    
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')
    
    
class IsOwnerFilterBackend(filters.BaseFilterBackend):
    
    """
    Filter that only allows users to see their own objects.
    """
    def filter_queryset(self, request, queryset, view):
        ###### TODO filter today date ##########
        # if you want to filter using query_params condition
        ###########################################
        # if request.query_params.get('data') == "oggi":
        #      queryset.filter(published_date=str(timezone.now()))
        #      print("post pubblicati in data odierna: {}".format(queryset))
        return queryset.filter(author=request.user.pk)
    

class PostApiView(ModelViewSet):
    queryset = Post.objects.filter(published_date__lte=timezone.now())
    serializer_class = PostSerializer
    filter_backends = (DjangoFilterBackend, IsOwnerFilterBackend)
    filterset_fields = ('author', 'title',)
    # permission_classes = [AllowAny]



