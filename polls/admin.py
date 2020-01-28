from django.contrib import admin

from .models import Choice, Question

#Question 5 Add these two lines
admin.site.register(Choice)
admin.site.register(Question)