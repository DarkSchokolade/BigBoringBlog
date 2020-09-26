from django.shortcuts import render, redirect

# Create your views here.
from .models import *
from .forms import *

# BigBoringBlog
def Home(request):
    # boards = Board.objects.all()
    boards = Board.objects.order_by('name')
    context = {'boards': boards}
    return render(request, 'BigBoringBlog/home.html', context)
    
def TopicsPage(request, p_key):
    board = Board.objects.get(id=p_key)

    topics = board.topics.all().order_by('-created_at')
    context = {'board': board, 'topics': topics}
    return render(request, 'BigBoringBlog/topics.html', context)

def CreateTopic(request, p_key):
    form = TopicForm()
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            board = Board.objects.get(id=p_key)
            topic.board = board
            topic.save()
            return redirect('BigBoringBlog:topics', p_key=p_key)

    context = {'form':form}
    return render(request, 'BigBoringBlog/create_topic.html', context)

def CommentSection(request, p_key):
    topic = Topic.objects.get(id=p_key)

    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.save()

    posts = topic.posts.all().order_by('-created_at')
    context = {'topic': topic, 'posts': posts, 'form':form}
    return render(request, 'BigBoringBlog/posts.html', context)

def AboutPage(request):
    return render(request, 'BigBoringBlog/about.html')