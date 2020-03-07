from django import forms
from .models import Post





class PostForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ('title', 'content', 'product', 'rating', 'media')