# Generated by Django 4.1.1 on 2023-07-16 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskman', '0005_alter_project_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
