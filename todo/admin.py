from django.contrib import admin
from .models import todo, notes, ideas_goals
# Register your models here.
@admin.register(todo)


class todomodel(admin.ModelAdmin):
   list_display = [f.name for f in todo._meta.fields]

@admin.register(notes)
class notesmodel(admin.ModelAdmin):
   list_display = ['title','notes']

@admin.register(ideas_goals)
class notesmodel(admin.ModelAdmin):
   list_display = ['ideas','goals']