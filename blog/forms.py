from django import forms
from .models import Post,Comment

class BlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'status')
        label = {"image":"Image URL"}

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('body',)
#         label = {"body":"Comment"}