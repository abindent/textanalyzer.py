# Welcome to Text Analyzer Docs!

This site was created using [**Docsify**](https://docsify.js.org), which is an open source documentation site generator, and imported in GitHub page. This site was created for docs about Text Analyzer.


<p align="center">
  <img max-width="100%" src="https://i.imgur.com/orfhf4u.png?1" />
</p>

# <img src="https://textanalyzerpy.herokuapp.com/static/favicon/favicon.png" width="30px" />Textanalyzer Django Project

## 🚀 About Me
I'm a a beginner developer for Python and Javascript...

  
## 🕵️‍ Skills
Javascript, HTML, CSS, Python...

## 🆕 Latest Project  

## DJANGO

# Django + BootStrap + Github + Heroku
![Logo](https://emojis.slackmojis.com/emojis/images/1483054030/1541/django.png)  ![Logo](https://emojis.slackmojis.com/emojis/images/1470681426/745/plus.png)  ![Logo](https://emojis.slackmojis.com/emojis/images/1483053257/1538/bootstrap.png)  ![Logo](https://emojis.slackmojis.com/emojis/images/1470681426/745/plus.png)  ![Logo](https://emojis.slackmojis.com/emojis/images/1587484871/8712/github.png)  ![Logo](https://emojis.slackmojis.com/emojis/images/1470681426/745/plus.png)  ![Logo](https://emojis.slackmojis.com/emojis/images/1465929657/511/heroku.png)

## Desciption
This is my project where I have made a heroku app and deployed all the things with the help of github. Here you can analyze your text, edit and style your text for free with customer care 
            [Go and Visit Now](https://textanalyzerpy.herokuapp.com)
            
## Author

- [@Think-With-Us (Abindent)](https://www.github.com/abindent)

  
## License and Main Dependencies


[![python](https://img.shields.io/github/pipenv/locked/python-version/Think-With-Us/django)](https://python.org)

- [![Dependencies](https://img.shields.io/static/v1?label=main-dependencies&message=django&color=green)](https://www.djangoproject.com/)

- [![Dependencies](https://img.shields.io/static/v1?label=main-dependencies&message=django-heroku&color=green)](https://pypi.org/project/django-heroku/)

- [![Dependencies](https://img.shields.io/static/v1?label=main-dependencies&message=gunicorn&color=green)](https://gunicorn.org/)

[![license](https://img.shields.io/static/v1?label=License&message=Github&color=blue)](https://github.com/Think-With-Us/django.git)

  
## 🔗 Links

- [![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sinchan-maitra-22a303217/)
- [![reddit](https://img.shields.io/reddit/subreddit-subscribers/Abindent?style=social)](https://reddit.com/r/Abindent)
- [![discord](https://img.shields.io/discord/843750265554206740)](https://discord.com/invite/dFW3gG7gPy) 
- [![youtube](https://img.shields.io/youtube/channel/subscribers/UCYCtnmYa44736S7GbfnbYoQ?style=social)](https://tiny.cc/discoHuge-YT)

## FAQ
***1) HOW TO USE THIS?***

*ANS* : 
**WATCH THIS _VIDEO_**
 https://user-images.githubusercontent.com/86192575/140603942-0c217435-ddd9-41de-ad74-8da2982eda32.mp4



***2) HOW TO HOST A WEBSITE WITH DJNAGO, GITHUB AND HEROKU?***

*ANS*: 
 
Don't worry [Github](https://github.com) is here.         
Follow the following steps to host your site fro free.
1) Install django and pipenv using
   
                pip install pipenv
    
                pip install django
                
       pipenv install django [For Creating Virtual Environment and Pipfile & Pipfile.lock]


2) Open the folder where you want to save your project and type cmd in the place of the folder's path and run this command
      
                        django-admin startproject <projectname>

3) After constructing your site add Procfile and type 

                           web: gunicorn <projectname>.wsgi 
![Logo](https://i.imgur.com/ggaGGBu.jpg)

 #ignore commands.txt that is a file temporarily I have created


4) Install gunicorn and whitenoise through pipenv as well as pip
              
                           pip/pipenv install  gunicorn   
                           pip/pipenv install  whitenoise
5) Then in your settings.py add this MIDDLEWARE

                         'whitenoise.middleware.WhiteNoiseMiddleware',       

6) Now you need to add STATIC_ROOT Path in settings.py to tell where to look for static files e.g, css, js, etc.
  
                        STATIC_ROOT = os.path.join(BASE_DIR, 'static')
7) Now add new “static” folder inside root directory of your project, if you don’t have and then run following command to collect all inbuilt static files related to django-admin
   
                           python/python3 manage.py collectstatic
8) Now add requirements.txt file to your root directory. So, that heroku could install all the required packages that they need to run this app on their server.
  
                               pip freeze > requirements.txt
            

9) Now you need to install git If you haven’t installed it. Go and Just install Git from its official website and install it:

Download Git From Here: [Click Here](https://git-scm.com/downloads)

Then go to github and create a new repository and push your code by running the following commands

                    git init
                    git add README.md (Optionl)
                    git add .
                    git commit -m "first commit"
                    git branch -M main
                    git remote add orgin <github repository link.git>
                    git push -u origin main

![Logo](https://i.imgur.com/qfBhht5.jpg)   

10) Create an app on heroku

![Logo](https://i.imgur.com/Hm37ITX.jpg)

![Logo](https://i.imgur.com/HML7ZzB.jpg)

11) Once you’ve selected name for your app then add your app_domain inside your ALLOWED_HOST in settings.py

                   ALLOWED_HOSTS = [
                          '127.0.0.1',
                          '<projectname>.herokuapp.com',
                      ]
12) Now again, commit and push these changes to your github

                          > git add .
                          > git commit -m "Allowed Hosts"
                          > git push -u origin main

13) Now you need connect that github repository to your heroku app. Where your configured django project is available.
![Logo](https://i.imgur.com/QTPKLP5.jpg) 

and click on connect after finding the repository
![Logo](https://i.imgur.com/Mnu11JG.jpg)                          
                   
14) Now scroll down and there you will see option Enable Automatic Deploys, click on it to enable this feature.

And Now whenever you will make and new changes in your repository then it will automatically fetch your changes and then will apply those changes to deployed app.
![Logo](https://i.imgur.com/yPulo8u.jpg)       

15) Finally click on the deploy branch button.

16) And now your site will be fully live on url: projectname.herokuapp.com.
![Logo](https://i.imgur.com/5Jx2Qjk.gif)

# THE END
