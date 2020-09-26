from django.db import models

# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Topic(models.Model):
    subject = models.CharField(max_length=255)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='topics') #  But if we don’t set a name for it, Django will generate it with the name: (class_name)_set
    created_by = models.CharField(max_length=100, default='Anonymous')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.subject

class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='posts')
    created_by = models.CharField(max_length=100, default='Anonymous')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.message