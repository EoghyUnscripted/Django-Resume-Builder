from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import *

# Skills
def skill_details(request, skill_id):

    skill_det = get_object_or_404(skill, pk=skill_id)
    context = {'skill':skill_det}
    
    return render(request, 'skills/skill.html', context)

# Employers
def employer(request):

    employment = job.objects
    context = {'employment':employment}

    return render(request, 'employer/employer.html', context)

# Education
def university(request):

    education = university.objects
    context = {'education':education}

    return render(request, 'university/university.html', context)

# Applications
def app(request, app_id): 

    resume = get_object_or_404(application, pk=app_id)
    context = {'resume':resume}

    return render(request, 'resume/resume.html', context)

def res(request, app_id): 

    resume = get_object_or_404(application, pk=app_id)
    context = {'resume':resume}

    return render(request, 'resume/res2.html', context)

def plain(request, app_id): 

    resume = get_object_or_404(application, pk=app_id)
    context = {'resume':resume}

    return render(request, 'resume/plain.html', context)

def cover(request, app_id): 

    resume = get_object_or_404(application, pk=app_id)
    context = {'resume':resume}

    return render(request, 'resume/cover.html', context)