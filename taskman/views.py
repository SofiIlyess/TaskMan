from typing import Any, Dict
from django.db import models
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import Project,Folder,User,Task,Proritie,Tag
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.shortcuts import redirect

from .forms import TaskForm

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    user = request.user
    projectslist = user.owned_projects.all()
    folderslist = Folder.objects.all()
    return render(request,'taskman/index.html',{'projects':projectslist,'folders':folderslist,'tasks':tasks})


class CreateProject(LoginRequiredMixin,CreateView):
    model = Project
    fields = ['name','description','status']
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['projects'] = self.request.user.owned_projects.all()
        context['folders'] = Folder.objects.all()
        return context
    

    def form_valid(self, form):
        form.instance.owner = self.request.user
        # form.instance.contributors.set(self.request.user)
        return super().form_valid(form)
    
class ProjectDetail(LoginRequiredMixin,DetailView):
    model = Project

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['projects'] = self.request.user.owned_projects.all()
        context['folders'] = Folder.objects.all()
        return context

class ProjectEdit(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model= Project
    fields = ['name','description','contributors','status']

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['projects'] = self.request.user.owned_projects.all()
        context['folders'] = Folder.objects.all()
        return context
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.owner:
            return True
        return False



class ProjectDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    success_url = '/'

    def test_func(self):
        pr = self.get_object()
        if self.request.user == pr.owner:
            return True
        return False
    
class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    # fields = ['title','description','due_date','priority','tags','project','is_completed']
    form_class = TaskForm

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['projects'] = self.request.user.owned_projects.all()
        context['folders'] = Folder.objects.all()
        return context
    
    def form_valid(self,form):
        form.instance.assigned_to = self.request.user
        return super().form_valid(form)
    
class TaskList(LoginRequiredMixin,ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'
    ordering = ['-create_on']

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['projects'] = self.request.user.owned_projects.all()
        context['folders'] = Folder.objects.all()
        return context

class PriorityCreate(LoginRequiredMixin,CreateView):
    model = Proritie
    fields = ('__all__')
    success_url = '/priority/new/'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['projects'] = self.request.user.owned_projects.all()
        context['folders'] = Folder.objects.all()
        context['priorities'] = Proritie.objects.all()
        return context
    
    def form_valid(self, form):
        return super().form_valid(form)
    
class PriorityUpdate(LoginRequiredMixin,UpdateView):
    model = Proritie
    fields = ('__all__')
    success_url = '/priority/new/'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['projects'] = self.request.user.owned_projects.all()
        context['folders'] = Folder.objects.all()
        context['priorities'] = Proritie.objects.all()
        return context
    
    def form_valid(self, form):
        return super().form_valid(form)

class PriorityDelete(LoginRequiredMixin,DeleteView):
    model = Proritie
    success_url = '/priority/new/'

def PriorityDeleteAll(request):
    Proritie.objects.all().delete()
    return redirect('priority-create')

class TagCreate(LoginRequiredMixin,CreateView):
    model = Tag
    fields = ('__all__')
    success_url = '/tag/new/'
    # extra_context = {'tags':Tag.objects.all()}

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['projects'] = self.request.user.owned_projects.all()
        context['folders'] = Folder.objects.all()
        context['tags']= Tag.objects.all()
        return context
    
    def form_valid(self, form):
        return super().form_valid(form)

class TagDelete(LoginRequiredMixin,DeleteView):
    model = Tag
    success_url = '/tag/new/'

class TagUpdate(LoginRequiredMixin,UpdateView):
    model = Tag
    fields = ('__all__')
    success_url = '/tag/new/'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['projects'] = self.request.user.owned_projects.all()
        context['folders'] = Folder.objects.all()
        context['tags']= Tag.objects.all()
        return context


    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

def TagsDeleteAll(request):
    Tag.objects.all().delete()
    return redirect('tag-create')