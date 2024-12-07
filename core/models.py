from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField(max_length=800, verbose_name="Контент")
    
    def __str__(self):
        return f"Автор: {self.author}"
    
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"