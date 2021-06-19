from django.contrib import admin
from .models import (application, app_Comments, awards, category, 
                     contact, core, course, cover_Letter, job, link, 
                     objective, profile, skill, university)

# Profile
@admin.register(profile)
class ProfilesAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile_Name', 'reference', 'title_Abstract')
    list_filter = ['id']
    list_editable = ['profile_Name']

@admin.register(objective)
class ObjectivesAdmin(admin.ModelAdmin):
    list_display = ('id', 'reference', 'abstract')
    list_filter = ['id']

@admin.register(contact)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'reference', 'contact_Type', 'contact_Info')
    list_filter = ['id', 'contact_Type']
    list_editable = ['contact_Type', 'contact_Info']

# Skills
@admin.register(skill)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('id', 'reference', 'skill_Name')
    list_filter = ['id', 'skill_Name']
    list_editable = ['skill_Name']

@admin.register(core)
class CoressAdmin(admin.ModelAdmin):
    list_display = ('id', 'reference', 'core_Name')
    list_filter = ['id', 'core_Name']
    list_editable = ['core_Name']

@admin.register(category)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('id','reference', 'category_Name')
    list_filter = ['id', 'category_Name']
    list_editable = ['category_Name']

# Employment
@admin.register(job)
class EmployersAdmin(admin.ModelAdmin):
    list_display = ('id', 'reference', 'job_Title', 'job_Employer')
    list_filter = ['id', 'job_Title', 'job_Employer']
    list_editable = ['job_Title', 'job_Employer']

# Education
@admin.register(university)
class UniversitiesAdmin(admin.ModelAdmin):
    list_display = ('id', 'reference', 'uni_Degree', 'uni_Name')
    list_filter = ['id']
    list_editable = ['uni_Degree', 'uni_Name']

# Independent
@admin.register(course)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('id', 'reference', 'status', 'course_Date', 'course_Name', 'course_Description')
    list_filter = ['id', 'course_Date', 'course_Name']
    list_editable = ['course_Date', 'course_Name', 'course_Description']

# Awards
@admin.register(awards)
class AwardsAdmin(admin.ModelAdmin):
    list_display = ('id', 'award_Year', 'award_Name', 'award_Description')
    list_filter = ['id', 'award_Date', 'award_Name']
    list_editable = ['award_Name', 'award_Description']

# Links
@admin.register(link)
class LinksAdmin(admin.ModelAdmin):
    list_display = ('id', 'reference', 'link_Name', 'link_URL', 'link_Comment')
    list_filter = ['id', 'link_Name']
    list_editable = ['link_Name', 'link_URL', 'link_Comment']

# Applications
@admin.register(application)
class ApplicationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'app_Date', 'app_Title', 'app_Employer', 'app_Job_Title', 'app_Status')
    list_filter = ['id', 'app_Date', 'app_Title', 'app_Employer', 'app_Job_Title', 'app_Status']
    list_editable = ['app_Date', 'app_Title', 'app_Employer', 'app_Job_Title', 'app_Status'] 

@admin.register(app_Comments)
class AppCommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'app_Comment_Date', 'reference', 'app_Comment')
    list_filter = ['id', 'app_Comment_Date']

@admin.register(cover_Letter)
class CoverLettersAdmin(admin.ModelAdmin):
    list_display = ('id', 'reference', 'cover_Title')
    list_filter = ['id', 'cover_Title']
    list_editable = ['cover_Title']