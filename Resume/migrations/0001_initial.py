# Generated by Django 3.1.1 on 2021-06-13 21:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='app_Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_Comment_Date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Comment Date')),
                ('app_Comment', models.TextField(max_length=1000, verbose_name='App Comments')),
            ],
            options={
                'verbose_name': 'App Comment',
                'verbose_name_plural': 'App Comments',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_Name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['category_Name'],
            },
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_Type', models.CharField(max_length=100, verbose_name='Type')),
                ('contact_Icon', models.CharField(blank=True, max_length=100, verbose_name='Icon')),
                ('contact_Link', models.CharField(blank=True, max_length=100, verbose_name='Link')),
                ('contact_Info', models.CharField(max_length=100, verbose_name='Info')),
            ],
            options={
                'verbose_name': 'Contact Detail',
                'verbose_name_plural': 'Contact Details',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_Progress', models.CharField(blank=True, choices=[('2', 'In Progress'), ('0', '---'), ('1', 'Completed'), ('3', 'Pending')], default='0', help_text='Complete, In Progress, Pending', max_length=200, verbose_name='Progress')),
                ('course_Date', models.DateField(blank=True, help_text='Date Completed, Anticipated Completion or Anticipated Start', null=True, verbose_name='Date')),
                ('course_Name', models.CharField(max_length=200, verbose_name='Title')),
                ('course_Organization', models.CharField(help_text='Issuer or Institution', max_length=200, verbose_name='Organization')),
                ('course_Description', models.TextField(blank=True, help_text='i.e. general description, specialization, grade, series, etc', max_length=200, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Course / Cert',
                'verbose_name_plural': 'Courses / Certs',
                'ordering': ['course_Date', 'course_Name'],
            },
        ),
        migrations.CreateModel(
            name='cover_Letter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_Title', models.CharField(max_length=100)),
                ('cover_Body', models.TextField(blank=True, help_text='Manually write your cover letter, or fill the prompts.', max_length=3000)),
                ('cover_Intro', models.TextField(blank=True, help_text='Introduce yourself and reason for applying.', max_length=3000)),
                ('cover_P1', models.TextField(blank=True, help_text='Explain what your interest is with the company.', max_length=3000)),
                ('cover_P2', models.TextField(blank=True, help_text='Explain how your current education will benefit the organization.', max_length=3000)),
                ('cover_P3', models.TextField(blank=True, help_text='Explain how your current experience will benefit the organization.', max_length=3000)),
                ('cover_Extra', models.TextField(blank=True, help_text='Extra paragraph if needed.', max_length=3000)),
                ('cover_Close', models.TextField(blank=True, help_text='Write in your closing paragraph and reiterate any claims.', max_length=3000)),
            ],
            options={
                'verbose_name': 'Cover Letter',
                'verbose_name_plural': 'Cover Letters',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_Image', models.ImageField(blank=True, upload_to='images/', verbose_name='Logo')),
                ('job_Employer', models.CharField(max_length=200, verbose_name='Employer')),
                ('job_Title', models.CharField(max_length=200, verbose_name='Title')),
                ('job_Location', models.CharField(blank=True, max_length=200, verbose_name='Location')),
                ('job_DOH', models.DateField(blank='True', null=True, verbose_name='Date of Hire')),
                ('job_DOL', models.DateField(blank=True, null=True, verbose_name='Date of Leaving')),
                ('job_Description', models.TextField(blank=True, max_length=3000, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Employment',
                'verbose_name_plural': 'Employers',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_Name', models.CharField(max_length=100, verbose_name='Name')),
                ('link_URL', models.CharField(max_length=100, verbose_name='URL')),
                ('link_Comment', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Comment')),
            ],
            options={
                'verbose_name': 'Link',
                'verbose_name_plural': 'Links',
                'ordering': ['link_Name'],
            },
        ),
        migrations.CreateModel(
            name='objective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objective_Summary', models.TextField(verbose_name='Summary')),
            ],
            options={
                'verbose_name': 'Objective',
                'verbose_name_plural': 'Objectives',
            },
        ),
        migrations.CreateModel(
            name='university',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uni_Image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Crest')),
                ('uni_Name', models.CharField(max_length=500, verbose_name='Institution')),
                ('uni_Location', models.CharField(blank='True', help_text='City, State', max_length=200, verbose_name='Location')),
                ('uni_Degree', models.CharField(max_length=500, verbose_name='Degree Program')),
                ('uni_Graduation', models.DateField(blank=True, help_text='If still attending, enter anticipated graduation date.', null=True, verbose_name='Graduation Date')),
                ('uni_GPA', models.FloatField(blank=True, null=True, verbose_name='GPA')),
                ('uni_Description', models.TextField(blank=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'University',
                'verbose_name_plural': 'Universities',
            },
        ),
        migrations.CreateModel(
            name='skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_Name', models.CharField(max_length=100, verbose_name='Name')),
                ('skill_Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resume.category')),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
                'ordering': ['skill_Name'],
            },
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_Name', models.CharField(max_length=100, verbose_name='Name')),
                ('profile_Title', models.CharField(blank=True, max_length=200, verbose_name='Title')),
                ('profile_Contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resume.contact', verbose_name='Contact List')),
                ('profile_Objective', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Resume.objective', verbose_name='Objective')),
            ],
            options={
                'verbose_name': 'Profile Header',
                'verbose_name_plural': 'Headers',
            },
        ),
        migrations.CreateModel(
            name='application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_Title', models.CharField(help_text='Enter a name for the resume.', max_length=100, verbose_name='Title')),
                ('app_Date', models.DateField(verbose_name='Date Applied')),
                ('app_Status', models.BooleanField(default=False, verbose_name='Rejected')),
                ('app_Employer', models.CharField(help_text='Which company are you applying to?', max_length=100, verbose_name='Job Employer')),
                ('app_Job_Title', models.CharField(max_length=100, verbose_name='Job Title')),
                ('app_Job_Number', models.CharField(blank=True, max_length=100, verbose_name='Req #')),
                ('app_Employer_Address', models.TextField(blank=True, max_length=100, verbose_name='Company Phone')),
                ('app_Job_Description', models.TextField(blank=True, help_text='Can copy/paste job post.', max_length=5000, verbose_name='Job Description')),
                ('app_Link', models.URLField(blank=True, null=True, verbose_name='Job URL')),
                ('app_Comments', models.ManyToManyField(blank=True, to='Resume.app_Comments', verbose_name='Comments')),
                ('app_Cover', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Resume.cover_letter', verbose_name='Cover Letter')),
                ('app_Education', models.ManyToManyField(to='Resume.university', verbose_name='University')),
                ('app_Experience', models.ManyToManyField(to='Resume.job', verbose_name='Work Experience')),
                ('app_Independent', models.ManyToManyField(to='Resume.course', verbose_name='Independent Learning')),
                ('app_Links', models.ManyToManyField(to='Resume.link', verbose_name='References')),
                ('app_Profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Resume.profile', verbose_name='Profile')),
            ],
            options={
                'verbose_name': 'Resume',
                'verbose_name_plural': 'Resumes',
                'ordering': ['-id'],
            },
        ),
    ]
