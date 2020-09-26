from django.urls import path
from . import views

app_name = 'BigBoringBlog'  # namespacing your app

urlpatterns = [
    path('', views.Home, name='home'),
    path('topics/<str:p_key>/', views.TopicsPage, name='topics'),
    path('create_topic/<str:p_key>/', views.CreateTopic, name='create_topic'),
    path('comments/<str:p_key>/', views.CommentSection, name='comments'),
    path('about/', views.AboutPage, name='about')
]