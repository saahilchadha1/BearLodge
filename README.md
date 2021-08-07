# BearLodge

## Getting started 

1. Clone the repo 

2. Create a new virtual environment 
```
python3 -m venv env
```
3. Source the environment 
 ```
source env/bin/activate
```
4. Install dependencies 
```
pip3 install -r requirements.txt
```
5. Run migrations 
```
python3 manage.py migrate
```
6. Seed the database
```
python3 manage.py loaddata seed
```
7. Start the development server 

```
python3 manage.py runserver 127.0.0.1:8000
```
## Admin view 

Navigate to [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) and log in with these credentials.
```
username: superusername
password: superuserpassword
```
Here, you can directly view and edit database entries for testing purposes. If you want to add to the seed data, edit `draw/fixtures/seeds.json`

## Dealing with models 

Models are Python objects that represent a database record. The Django documentation has more details.
- How to work with models: [https://docs.djangoproject.com/en/3.2/topics/db/queries/](https://docs.djangoproject.com/en/3.2/topics/db/queries/) 
- How to work with user authentication: [https://docs.djangoproject.com/en/3.2/topics/auth/default/](https://docs.djangoproject.com/en/3.2/topics/auth/default/)

## Passing data to template 

To access database data from an HTML template, you need to pass it through the view. 
[This website](https://learnbatta.com/course/django/django-pass-data-from-view-to-template/) discusses how to do that. 

## Files to look at 

- `draw/urls.py` has all the URL routes
- `draw/models.py` defines the database schema. The User table is part of Django auth and is pre-loaded, so it isn't defined here; look at the link above.
- `draw/templates/draw` has the HTML template files
