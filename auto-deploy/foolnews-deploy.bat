TITLE My System Info
ECHO Creating Django Project
django-admin startproject foolnews
ECHO Installing articles app
pip install --user django-articles-0.1.tar.gz
ECHO copy urls.py file
xcopy /s/Y %cd%\setup-files\urls.py %cd%\foolnews\foolnews
ECHO copy settings.py file
xcopy /s/Y %cd%\setup-files\settings.py %cd%\foolnews\foolnews
ECHO copy API json files
mkdir %cd%\foolnews\data
xcopy %cd%\setup-files\data %cd%\foolnews\data /E
ECHO change to project dir
cd foolnews
python manage.py migrate
python manage.py runserver