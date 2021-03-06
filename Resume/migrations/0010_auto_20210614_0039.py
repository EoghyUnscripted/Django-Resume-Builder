# Generated by Django 3.1.1 on 2021-06-14 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0009_auto_20210614_0037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='app_Awards',
        ),
        migrations.RemoveField(
            model_name='application',
            name='app_Cores',
        ),
        migrations.RemoveField(
            model_name='application',
            name='app_Education',
        ),
        migrations.RemoveField(
            model_name='application',
            name='app_Experience',
        ),
        migrations.RemoveField(
            model_name='application',
            name='app_Independent',
        ),
        migrations.RemoveField(
            model_name='application',
            name='app_Links',
        ),
        migrations.RemoveField(
            model_name='application',
            name='app_Notes',
        ),
        migrations.RemoveField(
            model_name='application',
            name='app_Profile',
        ),
        migrations.RemoveField(
            model_name='application',
            name='app_Skills',
        ),
        migrations.AlterField(
            model_name='course',
            name='course_Progress',
            field=models.CharField(blank=True, choices=[('2', 'In Progress'), ('1', 'Completed'), ('3', 'Pending')], help_text='Complete, In Progress, Pending', max_length=200, verbose_name='Progress'),
        ),
    ]
