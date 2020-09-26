from django.forms import ModelForm

from .models import Topic, Post

class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['subject', 'created_by']

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['message', 'created_by']