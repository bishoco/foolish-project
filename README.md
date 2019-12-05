## Motley Fool Developer Interview Project - Corey Bishop

Overview
This is a my Motley Fool Developer interview project It is a simple news website that diplays articles from a json data file. When you click on an article headline, the full article is displayed along with stock quotes related to the articled.

Since I'm new to python and django, I kept things pretty simple. Let me know if you have any questions.

I created User Stories and Acceptance Criteria for this project. That can be seen here: https://github.com/bishoco/foolish-project/wiki/User-Stories

I also created a task board which helped keep track of what I was doing (and my sanity). It can be seen here: https://github.com/bishoco/foolish-project/projects/1

I ran out of time to get this deployed someplace online (like heroku). I'll continue working on that. There are instructions at the bottom of this page to get the project running locally. 

**Features**

_Main page_
* Displays a main article
* The main article is the first article with the slug=10-promise. (This is driven via the db table ContentConfig where key = main-article-slug which can be changed in the admin)
* Three articles below.

_Detailed Article page_
* Displays full article text
* Displays stock quotes on the right side bar based on the instruments element in the article data
* User can enter comments at the bottom of the page

_Search function_
* Simple search function that displays search results

**Technical Specs**
* Django 2.2.7
* Python 3.8.0
* sqlite database
* bootstrap 4.4.1
* jquery 3.4.1
* popper.js 1.16.0

**Project Layout**
* articles - This is the app folder and where the core source code is
* data - This is where the API json files are stored
* foolnews - This is project folder
* auto-deploy - auto deploy the project locally. See instructions below.

**Running locally**
This project can be cloned and run locally. Python and Django need to be installed. Execute these commands in the project root:
* python manage.py migrate
* python manage.py runserver
* open the site at http://127.0.0.1:8000/

**Auto Deploy**
I created a batch script that creates a django project, installs the app, and gets the server running locally. It contains a tar of my app and installs it to the newly created django project. It's in the auto-deploy directory of this project. 
* run the foolnews-deploy.bat
* open the site at http://127.0.0.1:8000/

_Note: this installs my django-articles app to your user directory. To remove the app from your user directory run uninstall.bat_

