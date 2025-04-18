from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
import math
from django.utils import timezone

User = get_user_model()

@property
def reading_time(self):
        word_count = len(self.content.split())
        return math.ceil(word_count / 200)
def __str__(self):
        return self.title

class Blog(models.Model):
    CATEGORY_CHOICES = [
        ('Technology', 'Technology'),
        ('Travel', 'Travel'),
        ('Food', 'Food'),
        ('Lifestyle', 'Lifestyle'),
        ('Business', 'Business'),
        ('Health', 'Health & Wellness'),
        ('Education', 'Education'),

    ]
    
    category = models.CharField(
        max_length=50, 
        choices=CATEGORY_CHOICES, 
        default='Technology'
    )
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    author_name = models.CharField(max_length=100, default='Anonymous', blank=True)
    author_email = models.EmailField(default='anonymous@example.com', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=200, blank=True)
    likes = models.PositiveIntegerField(default=0)

class Comment(models.Model):
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"Comment: {self.content[:30]}"

    @property
    def reading_time(self):
        word_count = len(self.content.split())
        return math.ceil(word_count / 200)

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images/', default='default.jpg', blank=True)
    phone_no = models.CharField(max_length=10, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)   

    def __str__(self):
        return f"{self.user.username} Profile"  

class Bookmark(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='bookmarks')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Bookmarked: {self.blog.title}"
    
class Feedback(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    rating = models.IntegerField()
    feedback_message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.first_name} {self.last_name}({self.email})"
    
class ContactMessage(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    submitted_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"