# Generated by Django 3.1.1 on 2021-06-14 00:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0005_auto_20210614_0003'),
    ]

    operations = [
        migrations.CreateModel(
            name='core',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('core_Name', models.CharField(help_text='<strong>What is the name of the core skill you want to add?</strong><br/>', max_length=100, verbose_name='Name')),
                ('core_Description', models.TextField(help_text='<strong>Briefly describe how you used your skill.</strong><br/>', verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Core Skill',
                'verbose_name_plural': 'Core Skills',
                'ordering': ['core_Name'],
            },
        ),
        migrations.AddField(
            model_name='skill',
            name='skill_Description',
            field=models.TextField(blank=True, help_text='<strong>Give some details about your skill. How have you used it?</strong><br/>', verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_Progress',
            field=models.CharField(blank=True, choices=[('1', 'Completed'), ('2', 'In Progress'), ('3', 'Pending')], help_text='Complete, In Progress, Pending', max_length=200, verbose_name='Progress'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='skill_Category',
            field=models.ForeignKey(help_text='<strong>Create a category for your skill (i.e. front-end, backend, general, etc).</strong><br/>', on_delete=django.db.models.deletion.CASCADE, to='Resume.category'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='skill_Name',
            field=models.CharField(help_text='<strong>What is the name of the skill you want to add?</strong><br/>', max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='application',
            name='app_Cores',
            field=models.ManyToManyField(blank=True, help_text='<strong>Aim to limit to 5 core skills.</strong><br/>', related_name='Core_Skills', to='Resume.core', verbose_name='Core Skills'),
        ),
    ]
