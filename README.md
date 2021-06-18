# The Hulbert Files
# Django-Resume-Builder
# Author: Eoghan Hulbert
# Version: 1.0
# Released: June 17, 2021

Thank you for checking out my resume builder with Django and Python.
This project is still active and in development, so some files make be blank or incomplete.
Feel free to clone this project if you want to practice or test the app, but please provide
feedback so that I can adjust and correct!

v1.0
The current version of this app has only 1 resume and cover letter layout but more are to be added
once I develop a front-end GUI for users.

This GUI will allow users to select and change the designs and colors of their resumes. 
These will be pre-set styles and will not be 100% customizable.

As of now, users will need to enter data in via manual coding or using the django-admin interface.
This is default as localhost:####/admin/ using the url scheme.

Users are able to create resumes and cover letters with the defaul style, including a plain/stripped
template. However, the template is dynamic -- if the content is not there, it will not display.

FIRST TIME USE:

To use this application, you will need to take steps to setting up your environments before running.

1) Create a local_settings.py file in the "Portal" main folder where you will see settings.py

2) In the local_settings.py file:
    a) create your secret key
    b) add allowed hosts
    c) set debugging environment (True if testing, False if production)
    d) and set up your database and credentials
   The information in these sub-steps will be hidden by the .gitignore file which will prevent
   your local_settings.py file from uploading or being read

3) Once these are set up, run the terminal command "pip install -r requirements.txt"
   This command will run through and install the components needed for the environment, including
   the virtualenv which is necessary to run the application

4) Next, create your virtual environment by running the terminal command: "virtualenv name"
   Replace "name" with the name you want for your virtual environment, you can even go with "env"
   This will create the virtual environment folders for you

5) Activate the virtual environment using terminal code: "source name/bin/activate"
   Again, "name" will be whatever the name was you gave the virtual environment
   You will know it worked because you will see (name) appear to the left of your username in the
   terminal

6) Repeat step 3 to make sure the virtual env is up-to-date

7) Run the terminal command: "python manage.py makemigrations",
   next, "python manage.py migrate",
   then, "python manage.py createsuper user"

8) Once all steps have been completed, enter in the command: "python manage.py runserver"
   This will initialize the server and host the project on localhost:8000 by default
   You can also designate the address by including it at the end of the command: 
        "python manage.py runserver yourip:8000"
    When designating this type of command, you allow other devices to access the application,
    such as your mobile device and other computers on your network by entering in the address:
        "http://yourip:8000/admin"

APPLICATION USE:

This application was designed to be scaleable, meaning if you wanted to add new components, you can.
As you explore each class, you will notice reference options. These options link each part to the main
object, which is the "Application".

As I was using this app to create new resumes and cover letters for each application I submitted for
jobs, I needed to keep them static so that any updates made, would only appear on a specific application.

This can become an issue the more applications and references that are in the app, and is something I 
am proactively working on resolving to avoid confusion and stress when using the application for it's
primary purpose.

1) Start with the "Resumes" - this is where you would enter in the details of the company you are applying
   to for this "application"

2) Next, create you "Profile Header" -- This is the top of the page with your name and your chosen title
   This page will also have a spot for phonetic pronuniation of your name, just in case yours is uncommon
   like mine

3) Add "Contact Details" - These will show up just under your name and should have at least your email
   address so that recruiters know how to reach you

4) Optional: Next, create an "Objective" -- This will appear under the contact details and will be where you
             can introduce yourself, explain your career goals, or just a brief description of you as a
             potential candidate for the role

5) Optional: Add up to 5 primary skills in the "Core Skills" section, and include a brief description of
             each so that recruiters and managers know how they apply to the job role

6) Optional: Add the skills related directly to the job role you are applying for -- if you are a developer
             you can add your technical skills. Otherwise, you can leave emppty or continue to list the rest
             of your skills related to the job role
    
    NOTE: If you do not link the skills to a set category, they will not display on the resume
          You can set a category with the title of "General" or add a fontawesome icon in it's place

7) Optional: Add employment to your resume -- This section is optional, but should include some form of
             activity, such as professional employment, volunteer work, work study, self-employment, 
             internships, etc
             Be sure to check off whether or not it is a current role for display purposes

8) Optional: Add education to your resume -- This section is optional, but should include some form of
             activity, such as college courses, paid training courses, internships, etc

9) Optional: Add independent study to your resume -- This section is optional, but can include other forms of
             training, such as personal projects, research projects, online courses through Udemy, etc

10) Optional: Add awards and accolades to your resume -- This section is optional, but can include items that
              demonstrate your abilities such as winning an award for desinging a website for your local youth
              center, participating in the 100 days of coding challenge, etc

11) Optional: Lastly, add add your reference links -- This section is optional, but can include social links,
              Github repository, portfolio links, etc

Thank you, again for checking out my work. If you have questions, concerns, or suggestions, please reach out to me!
