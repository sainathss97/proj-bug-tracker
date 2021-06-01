from django.contrib import admin
from .models import Task,Bug
# Register your models here.
admin.site.register(Task)
admin.site.register(Bug)