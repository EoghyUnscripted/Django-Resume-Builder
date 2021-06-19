from django.db import models
from django.db.models.deletion import CASCADE
from datetime import datetime, date

# Profile
class contact(models.Model):
    contact_Type = models.CharField('Type', help_text='<strong>Phone, Email, Address, etc.</strong><br/>', max_length=100)
    contact_Info = models.CharField('Info', help_text='<strong>Add your contact detail here, (i.e. phone number, email address, home address, etc).</strong><br/>', max_length=100)
    contact_Profile_Ref = models.ForeignKey('profile', max_length=200, help_text='<strong>What profile do you want to attach this to?</strong><br/>', related_name='contact',
                                            on_delete=CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Contact Detail'
        verbose_name_plural = 'Contact Details'
        ordering = ['id']

    def __str__(self):
        label = self.contact_Type + ' - ' + self.contact_Info
        return label

    def reference(self):
        label = self.contact_Profile_Ref.profile_App_Ref.app_Title
        return label

class objective(models.Model):
    objective_Summary = models.TextField('Summary')
    objective_Profile_Ref = models.ForeignKey('profile', max_length=200, help_text='<strong>What profile do you want to attach this to?</strong><br/>', related_name='obj',
                                                 on_delete=CASCADE, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Objective'
        verbose_name_plural = 'Objectives'
    
    def __str__(self):
        label = self.objective_Summary[:100]
        return label

    def abstract(self):
        return self.objective_Summary[:200] + '...'

    def reference(self):
        label = self.objective_Profile_Ref.profile_App_Ref.app_Title
        return label
        
class profile(models.Model):
    profile_Name = models.CharField('Name', help_text='<strong>What name should be on your resume?</strong><br/>', max_length=100)
    profile_Phonetic = models.CharField('Phonetic Name', help_text='<strong>How do we pronounce your name?</strong><br/>', max_length=100, blank=True)
    profile_Title = models.CharField('Title', max_length=200, help_text='<strong>What is the job title you are aiming for?</strong><br/>', blank=True)
    profile_App_Ref = models.ForeignKey('application', max_length=200, help_text='<strong>What app do you want to attach this to?</strong><br/>', related_name='pro', 
                                         on_delete=CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Profile Header'
        verbose_name_plural = 'Profile Headers'
        ordering = ['-id']

    def __str__(self):
        label = str(self.profile_App_Ref)
        return label

    def title_Abstract(self):
        label = self.profile_Title[:50]
        return label

    def reference(self):
        label = self.profile_App_Ref.app_Title
        return label

# Skills
class category(models.Model):

    category_Name = models.CharField(max_length=100)
    category_App_Ref = models.ForeignKey('application', max_length=200, help_text='<strong>What application do you want to attach this to?</strong><br/>', related_name='cat',
                                                 on_delete=CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['category_Name', '-id']

    def __str__(self):
        return str(self.category_App_Ref) + ' - ' + str(self.category_Name)

    def reference(self):
        label = self.category_App_Ref.app_Title
        return label

class core(models.Model):

    core_Name = models.CharField('Name', help_text='<strong>What is the name of the core skill you want to add?</strong><br/>', max_length=100)
    core_Description = models.TextField('Description', help_text='<strong>Briefly describe how you used your skill.</strong><br/>')
    core_App_Ref = models.ForeignKey('application', max_length=200, help_text='<strong>What app do you want to attach this to?</strong><br/>', related_name='core',
                                                 on_delete=CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Core Skill'
        verbose_name_plural = 'Core Skills'
        ordering = ['id', 'core_Name']

    def __str__(self):
        label = self.core_Name
        return label

    def reference(self):
        label = self.core_App_Ref.app_Title
        return label

    def category_Sort(category_id):

        categories = core.objects.all().filter(core_Category=category_id)
        
        sorted = {'category':categories}

        return sorted

class skill(models.Model):

    skill_Name = models.CharField('Name', help_text='<strong>What is the name of the skill you want to add?</strong><br/>', max_length=100)
    skill_Description = models.TextField('Description', help_text='<strong>Give some details about your skill. How have you used it?</strong><br/>', blank=True)
    skill_Category_Ref = models.ForeignKey(category, max_length=200, help_text='<strong>What category do you want to attach this to?</strong><br/>', related_name='skill',
                                                 on_delete=CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        ordering = ['skill_Name', '-id']

    def __str__(self):
        label = self.skill_Name
        return label
    
    def reference(self):
        label =  str(self.skill_Category_Ref)
        return label

    def category_Sort(category_id):

        categories = skill.objects.all().filter(skill_Category=category_id)
        
        sorted = {'category':categories}

        return sorted

# Employment
class job(models.Model):
    job_Image = models.ImageField('Logo', upload_to='images/', blank=True)
    job_Employer = models.CharField('Employer', max_length=200)
    job_Title = models.CharField('Title', max_length=200)
    job_Location = models.CharField('Location', max_length=200, blank=True)
    job_DOH = models.DateField('Date of Hire', blank='True', null=True)
    job_DOL = models.DateField('Date of Leaving', blank=True, null=True)
    job_Description = models.TextField('Description', blank=True, max_length=3000)
    job_Current = models.BooleanField('This Is My Current Employer')
    job_App_Ref = models.ForeignKey('application', max_length=200, help_text='<strong>What application do you want to attach this to?</strong><br/>', related_name='job',
                                                 on_delete=CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Employment'
        verbose_name_plural = 'Employers'
        ordering = ['-job_DOL', '-job_DOH']

    def __str__(self):
        label = str(self.id) + ' - ' + self.job_Title
        return label

    def doh_y(self):
        if self.job_DOH is None:
            return 'Unknown Start'
        else:
            label = self.job_DOH.strftime('%b, %Y')
            return label

    def dol_y(self):
        if self.job_DOL is None:
            if self.job_Current == 1:
                return 'Present'
            else:
                return 'Unknown End'
        else:
            label = self.job_DOL.strftime('%b, %Y')
            return label
    
    def job_Duration(self):
        doh = self.doh_y()
        dol = self.dol_y()

        label = str(doh + ' - ' + dol)
        return label

    def job_Split(self):
        label = self.job_Description.split(";")
        return label

    def reference(self):
        label = self.job_App_Ref.app_Title
        return label

    def job_Status(self):
        if self.job_Current == '1':
            return True
        if self.job_Current == '0': 
            return False
        

# Education
class university(models.Model):
    uni_Image = models.ImageField('Crest', upload_to='images/', blank=True, null=True)
    uni_Name = models.CharField('Institution', max_length=500)
    uni_Location = models.CharField('Location', help_text='City, State', max_length=200, blank='True')
    uni_Degree = models.CharField('Degree Program', max_length=500)
    uni_Start = models.DateField('Start Date', blank=True, null=True)
    uni_Graduation = models.DateField('Graduation Date', help_text='If still attending, enter anticipated graduation date.', blank=True, null=True)
    uni_GPA = models.FloatField('GPA', blank=True, null=True)
    uni_Description = models.TextField('Description', blank=True)
    uni_App_Ref = models.ForeignKey('application', max_length=200, help_text='<strong>What application do you want to attach this to?</strong><br/>', related_name='uni',
                                                 on_delete=CASCADE, blank=True, null=True)


    class Meta:
        verbose_name = 'University'
        verbose_name_plural = "Universities"

    def __str__(self):
        label = self.uni_Degree
        return label

    def uni_Begin(self):
        if self.uni_Start is None:
            label = 'Unknown Start'
            return label
        else:
            label = self.uni_Start.strftime('%b, %Y')
            return label
    
    def uni_End(self):
        if self.uni_Graduation is None:
            label = 'Unknown End'
            return label
        else:
            label = self.uni_Graduation.strftime('%b, %Y')
            return label

    def uni_Duration(self):
        start = self.uni_Begin()
        end = self.uni_End()

        label = str(start + ' - ' + end)
        return label
    
    def reference(self):
        label = self.uni_App_Ref.app_Title
        return label

# Independent Courses / Certifications
class course(models.Model):

    progress = {
        ('Completed', 'Completed'),
        ('In Progress', 'In Progress'),
        ('Pending', 'Pending')
    }

    course_Progress = models.CharField('Progress', choices=progress, help_text='Complete, In Progress, Pending', max_length=200, blank=True)
    course_Date = models.DateField('Date', help_text='Date Completed, Anticipated Completion or Anticipated Start', blank=True, null=True)
    course_Name = models.CharField('Title', max_length=200)
    course_Organization = models.CharField('Organization', help_text='Issuer or Institution', max_length=200)
    course_Description = models.TextField('Description', help_text='i.e. general description, specialization, grade, series, etc', max_length=200, blank=True)
    course_App_Ref = models.ForeignKey('application', max_length=200, help_text='<strong>What application do you want to attach this to?</strong><br/>', related_name='ind',
                                                 on_delete=CASCADE, blank=True, null=True)


    class Meta:
        verbose_name = 'Course / Cert'
        verbose_name_plural = 'Courses / Certs'
        ordering = ['course_Date', 'course_Name']

    def __str__(self):
        label = self.course_Name + ' - ' + self.course_Description
        return label

    def status(self):
        return self.course_Progress

    def course_Year(self):
        return self.course_Date.strftime('%Y')

    def faIcon(self):
        if self.course_Progress == 'Completed':
            label = "<i class='fad fa-check-square fa-fw'></i>"
            return label             
            
        elif self.course_Progress == 'In Progress':
            label = "<i class='fad fa-square fa-fw'></i>"
            return label

        elif self.course_Progress == 'Pending':
            label = "<i class='fad fa-spinner fa-fw'></i>"
            return label

        elif self.course_Progress == '---':
            label = "<i class='fad fa-spinner fa-fw'></i>"
            return label

    def reference(self):
        label = self.course_App_Ref.app_Title
        return label

# Awards
class awards(models.Model):

    award_Date = models.DateField('Date', help_text='When did you receive the award?', blank=True, null=True)
    award_Name = models.CharField('Title', help_text='What is the name of the award?', max_length=200)
    award_Organization = models.CharField('Organization', help_text='Issuer or Institution', max_length=200)
    award_Description = models.TextField('Description', help_text='i.e. general description, specialization, grade, series, etc', max_length=200, blank=True)
    award_App_Ref = models.ForeignKey('application', max_length=200, help_text='<strong>What application do you want to attach this to?</strong><br/>', related_name='award',
                                                 on_delete=CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Award'
        verbose_name_plural = 'Awards'
        ordering = ['-award_Date', 'award_Name']

    def __str__(self):
        label = self.award_Name + ' - ' + self.award_Description
        return label

    def award_Year(self):
        return self.award_Date.strftime('%Y')

    def reference(self):
        label = self.award_App_Ref.app_Title
        return label

# Links
class link(models.Model):
    link_Name = models.CharField('Name', max_length=100)
    link_URL = models.CharField('URL', max_length=100)
    link_Comment = models.TextField('Comment', max_length=1000, null=True, blank=True)
    link_App_Ref = models.ForeignKey('application', max_length=200, help_text='<strong>What application do you want to attach this to?</strong><br/>', related_name='link',
                                      on_delete=CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'
        ordering = ['link_Name']

    def __str__(self):
        return self.link_URL

    def reference(self):
        label = self.link_App_Ref.app_Title
        return label

# Application
class app_Comments(models.Model):

    app_Comment_Date = models.DateTimeField('Comment Date', default=datetime.now)
    app_Comment = models.TextField('App Comments', max_length=1000)
    app_Ref = models.ForeignKey('application', help_text='<strong>What app does this belong to?</strong>', verbose_name='App References', on_delete=CASCADE, null=True)

    class Meta:
        verbose_name = 'App Comment'
        verbose_name_plural = 'App Comments'
        ordering = ['-id']

    def __str__(self):
        label = str(self.app_Comment_Date.strftime("%Y-%m-%d")) + ' - ' + self.app_Ref.app_Title + ' - ' + self.app_Comment
        return label

    def reference(self):
        label = self.app_Ref.app_Title
        return label

class cover_Letter(models.Model):

    cover_Title = models.CharField(max_length=100)
    cover_Body = models.TextField(help_text='Manually write your cover letter, or fill the prompts.', max_length=3000, blank=True)
    cover_Intro = models.TextField(help_text='Introduce yourself and reason for applying.', max_length=3000, blank=True)
    cover_P1 = models.TextField(help_text='Explain what your interest is with the company.', max_length=3000, blank=True)
    cover_P2 = models.TextField(help_text='Explain how your current education will benefit the organization.', max_length=3000, blank=True)
    cover_P3 = models.TextField(help_text='Explain how your current experience will benefit the organization.', max_length=3000, blank=True)
    cover_Extra = models.TextField(help_text='Extra paragraph if needed.', max_length=3000, blank=True)
    cover_Close = models.TextField(help_text='Write in your closing paragraph and reiterate any claims.', max_length=3000, blank=True)
    cover_App_Ref = models.OneToOneField('application', max_length=200, help_text='<strong>What application do you want to attach this to?</strong><br/>', related_name='cov',
                                                 on_delete=CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Cover Letter'
        verbose_name_plural = 'Cover Letters'
        ordering = ['-id']

    def __str__(self):
        return self.cover_Title

    def letter_body(self):
        if self.cover_Body != '':
            return self.cover_Body
        elif self.cover_Body == '':
            Intro = self.cover_Intro
            PG1 = self.cover_P1
            PG2 = self.cover_P2
            PG3 = self.cover_P3
            Extra = self.cover_Extra
            Close = self.cover_Close
            body = Intro + PG1 + PG2 + PG3 + Extra + Close
            return body

    def reference(self):
        label = self.cover_App_Ref.app_Title
        return label

class application(models.Model):

    app_Title = models.CharField('Resume Title', help_text='<strong>Enter a name for the resume.</strong>', max_length=100)
    app_Date = models.DateField('Date Applied')
    app_Status = models.BooleanField('Rejected', help_text='<strong>Check if your application has been rejected.</strong>', default=False)
    app_Employer = models.CharField('Company Name', help_text='<strong>Which company are you applying to?<br/>This will be used on the cover letter.</strong>', max_length=100)
    app_Job_Title = models.CharField('Job Title', help_text='<strong>This will be used on the cover letter.</strong>', max_length=100)
    app_Job_Number = models.CharField('Job ID #', max_length=100, help_text='<strong>This will be on the job post if one is given.</strong>', blank=True)
    app_Employer_Address = models.TextField('Company Address', help_text='<strong>Usually the office you are applying to or HQ if remote role.</strong>', max_length=100, blank=True)
    app_Employer_Phone = models.CharField('Company Phone', help_text='<strong>Primary company contact number to reach Human Resources.</strong>', max_length=100, blank=True)
    app_Job_Description = models.TextField('Job Description', help_text='<strong>You can copy/paste job post details here.</strong>', max_length=5000, blank=True)
    app_Link = models.URLField('Job URL', help_text='<strong>What is the link to the job posting?</strong>', blank=True, null=True)
    app_Cover = models.OneToOneField(cover_Letter, verbose_name='Cover Letter', on_delete=CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Resume'
        verbose_name_plural = 'Resumes'
        ordering = ['-id']

    def __str__(self):
        return str(self.id) + '. ' + self.app_Title
