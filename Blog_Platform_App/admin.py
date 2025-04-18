from django.contrib import admin
from .models import Feedback
from .models import Profile
from django.contrib.auth.models import User

admin.site.register(Feedback)
admin.site.register(Profile)


