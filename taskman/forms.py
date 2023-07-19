from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title','description','due_date','priority','tags','project','folder','is_completed')
        widgets = {
            'title':forms.TextInput(),
            'description':forms.Textarea(),
            'due_date':forms.DateInput(attrs={'type':'date'}),
            'priority':forms.Select(),
            'project':forms.Select(),
            'is_completed':forms.CheckboxInput(attrs={'style':'margin-left:1vh;margin-top:-1px;'})
        }