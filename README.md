# Apps
## polls
official tutorials
## denglu
log in sample
## denglu2
log in with AD account
## psql01
multiple DB connection

# tips

* Basic
```python
    python manage.py runserver              # run web service   
    python manage.py startapp polls         # create new app (polls) 
    python manage.py createsuperuser        # create admin  
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