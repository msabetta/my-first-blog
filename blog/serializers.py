from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    
    class Meta:
        model = Post
        fields = ('author','title')
    
    # print(Post.objects.filter(title__contains="tests")[0].author)