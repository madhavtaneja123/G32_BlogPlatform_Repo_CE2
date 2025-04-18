from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Blog, Comment, Feedback, Profile 

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'phone_no', 'bio', 'linkedin', 'instagram', 'facebook']

    def clean_linkedin(self):
        linkedin = self.cleaned_data.get('linkedin')
        return linkedin or None

    def clean_instagram(self):
        instagram = self.cleaned_data.get('instagram')
        return instagram or None

    def clean_facebook(self):
        facebook = self.cleaned_data.get('facebook')
        return facebook or None

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['author_name', 'author_email', 'title', 'category', 'tags', 'content']
        widgets = {
            'author_name': forms.TextInput(attrs={
                'class': 'form-control',
                'readonly': True
            }),
            'author_email': forms.EmailInput(attrs={
                'class': 'form-control',
                'readonly': True
            }),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'tags': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 12}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['first_name', 'last_name', 'email', 'rating', 'feedback_message']