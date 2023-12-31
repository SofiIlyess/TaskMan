"""tasknoteman URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from taskman.views import (
                            index,CreateProject,ProjectDetail,ProjectEdit,ProjectDelete,
                            CreateTask,TaskList,PriorityCreate,TagCreate,TagDelete,TagUpdate,TagsDeleteAll,
                            PriorityUpdate,PriorityDelete,PriorityDeleteAll
                        )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('project/new/',CreateProject.as_view(),name='project-new'),
    path('project/<int:pk>/',ProjectDetail.as_view(),name='project-detail'),
    path('project/<int:pk>/edit',ProjectEdit.as_view(),name='project-edit'),
    path('project/<int:pk>/delete',ProjectDelete.as_view(),name='project-delete'),
    path('task/new/',CreateTask.as_view(),name='task-create'),
    path('tasks/',TaskList.as_view(),name='tasks-list'),
    path('priority/new/',PriorityCreate.as_view(),name='priority-create'),
    path('priority/<int:pk>/edit',PriorityUpdate.as_view(),name='priority-edit'),
    path('priority/<int:pk>/delete',PriorityDelete.as_view(),name='priority-delete'),
    path('priority/deleteAll',PriorityDeleteAll,name='priority-delete-all'),
    path('tag/new/',TagCreate.as_view(),name='tag-create'),
    path('tag/<int:pk>/delete',TagDelete.as_view(),name='tag-delete'),
    path('tag/<int:pk>/edit',TagUpdate.as_view(),name='tag-edit'),
    path('tag/deleteAll',TagsDeleteAll,name='tag-delete-all',)
]
