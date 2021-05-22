from posts.models import Post
from django import forms

class PostForm(forms.ModelForm):
    

    class Meta:
        model = Post
        fields = ['title', 'content'] #모든 요소를 넣고 싶다고 하면 '__all__' 이라 써주면 된다.