# Generated by Django 4.1.4 on 2023-07-18 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskman', '0010_alter_task_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='folder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='taskman.folder'),
        ),
    ]