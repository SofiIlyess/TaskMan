from django.db import models
from django.contrib.auth.models import User
import datetime
from django.urls import reverse

class Proritie(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    due_date = models.DateTimeField(blank=True,null=True)
    priority = models.ForeignKey(Proritie, on_delete=models.SET_NULL,null=True,blank=True)
    tags = models.ManyToManyField('Tag',blank=True,null=True)
    project = models.ForeignKey('Project', on_delete=models.CASCADE,null=True,blank=True)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    completed_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Project(models.Model):
    class Status(models.IntegerChoices):
        INP = 1, "IN PROGRESS"
        INH = 2, "IN HOLD"
        COM = 3, "COMPLETED"
    
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_projects')
    contributors = models.ManyToManyField(User, related_name='projects',blank=True,null=True)
    createon = models.DateTimeField(default=datetime.datetime.now)
    status = models.PositiveSmallIntegerField(choices=Status.choices,default=Status.INP)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk': self.pk})
    

class Folder(models.Model):
    name = models.CharField(max_length=255,unique=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='folders')

    def __str__(self):
        return self.name