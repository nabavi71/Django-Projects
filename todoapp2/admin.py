from django.contrib import admin
from .models import TodoTask

# Register your models here.

class TodoTaskAdmin(admin.ModelAdmin):
    pass

admin.site.register(TodoTask, TodoTaskAdmin)


