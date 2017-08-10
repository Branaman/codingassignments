cd C:\Users\mbran\Desktop\DojoAssignments\Python\python_stack\myEnvironments
call djangoEnv/scripts/activate
cd ..\..\Django
django-admin startproject %1
cd %1
mkdir apps
cd apps
python ..\manage.py startapp %2
nul> __init__.py
cd %2
nul> urls.py
mkdir templates
cd templates
mkdir %2
cd %2
nul> index.html
cd ..\..\..\..
python manage.py runserver
pause
