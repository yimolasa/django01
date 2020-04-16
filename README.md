# Apps
## polls
official tutorials
* <http://127.0.0.1:8000/polls/>
## denglu
log in sample
* [index][dlindex]
* [login][dllogin]
* [register][dlregister]
* [all user list][dlal]
* [user page][dlul]

[dlindex]: http://127.0.0.1:8000/dl/ '/dl/'
[dllogin]: http://127.0.0.1:8000/dl/login/ '/dl/login/'
[dlregister]: http://127.0.0.1:8000/dl/register/ '/dl/register/'
[dlal]: http://127.0.0.1:8000/dl/login/ '/dl/login/'
[dlul]: http://127.0.0.1:8000/dl/login/user/ '/dl/login/user/'

## denglu2
log in with AD account
* [dl2](http://127.0.0.1:8000/dl2/ '/dl2')
## psql01
multiple DB connection
* [psql01](http://127.0.0.1:8000/psql01/ '/psql01')
# tips

* Display README.md in VScode

    Ctrl + Shift + V

* Basic
```python
    django-admin startproject djg01         # initial project
    python manage.py startapp polls         # create new app (polls) 
    python manage.py createsuperuser        # create admin  
    python manage.py runserver              # run web service
```
* Play with database
```python
    python manage.py makemigrations polls   # check changes of INSTALLED_APPS (polls) && generate a migration file  
    python manage.py sqlmigrate polls 0001  # display these changes (CREATE TABLE "polls_question" ("id" integer NOT NULL PRIMARY KEY AUTOINCRE......))        
    python manage.py migrate                # operate with database based on the migration file 
```

* Pre-install
```python
    pip install PyMySQL                     # for mysql
    pip install psycopg2                    # for PostgreSQL
```