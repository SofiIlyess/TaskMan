from django.contrib import admin
from .models import Proritie,Project,Tag,Task,Folder

# Register your models here.
admin.site.register(Proritie)
admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(Task)
admin.site.register(Folder)