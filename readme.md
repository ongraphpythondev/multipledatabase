#Description
##This is a multiple databases poc
###In this poc, three databases are used 1 for user,2 and 3 for the apps
for using this project firstly clone this project
```bash
git clone https://github.com/ongraphpythondev/multipledatabase
```
after cloning the project you have to make migrations and **migrate** the **databases**
```bash
python manage.py makemigrations
python manage.py migrate --database=db1
python manage.py migrate --database=db2
python manage.py migrate --database=db3
```
for creating admin
```bash
python msnsge.py createsuperuser --database=db1
```
After configuring the databases now you have to run server
```bash
python manage.py runserver
```
Now you have done
Go to following url 
http://127.0.0.1:8000/first/view  for view all the data of the database 2
http://127.0.0.1:8000/first/create for insert the data in the database 2

http://127.0.0.1:8000/second/view  for view all the data of the database 3
http://127.0.0.1:8000/second/create for insert the data in the database 3

**The first database (db1) is used for admin,user,session,authentication**
