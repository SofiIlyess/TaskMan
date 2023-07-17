from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import Project,Folder,User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


# Create your views here.
def index(request):
    user = request.user
    projectslist = user.owned_projects.all()
    folderslist = Folder.objects.all()
    return render(request,'taskman/index.html',{'projects':projectslist,'folders':folderslist})


class CreateProject(LoginRequiredMixin,CreateView):
    model = Project
    fields = ['name','description','status']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        # form.instance.contributors.set(self.request.user)
        return super().form_valid(form)
    
class ProjectDetail(LoginRequiredMixin,DetailView):
    model = Project


class ProjectEdit(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model= Project
    fields = ['name','description','contributors','status']

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