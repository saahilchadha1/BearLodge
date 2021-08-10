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

## Files to look at 

- `draw/urls.py` has all the URL routes
- `draw/models.py` defines the database schema. The User table is part of Django auth and is pre-loaded, so it isn't defined here; look at the link above.
- `draw/templates/draw` has the HTML template files

## Admin view 

Navigate to [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) and log in with these credentials.
```
username: superusername
password: superuserpassword
```
Here, you can directly view and edit database entries for testing purposes. If you want to add to the seed data, edit `draw/fixtures/seeds.json`

## Sample Users

`User` records are managed by Django auth, and `Profile` records are created and managed by us. The `Profile` record has a `user` field that has a 1-1 relationship with the `User` table, and it has an `is_seller` flag indicating whether the user is a seller or buyer. There's two sample users, a seller and a buyer. Here are the credentials 

Seller
```
username: sarah
password: test9999
```

Buyer
```
username: robert
password: abc123
```

## Dealing with models 

Models are Python objects that represent a database record. The Django documentation has more details.
- How to work with models: [https://docs.djangoproject.com/en/3.2/topics/db/queries/](https://docs.djangoproject.com/en/3.2/topics/db/queries/) 
- How to work with user authentication: [https://docs.djangoproject.com/en/3.2/topics/auth/default/](https://docs.djangoproject.com/en/3.2/topics/auth/default/)

## Passing data to template 

To access database data from an HTML template, you need to pass it through the view. 
[This website](https://learnbatta.com/course/django/django-pass-data-from-view-to-template/) discusses how to do that. 



--------------------------------------------------------------------
Part 1 index, login, register -- Documentation

## unfinished features
1. check if user has a Berkeley email address. For buyer, they have to have one.
        But for seller, they don't need to have 
2. logout feature
3. page layout modification -- back buttons, html && css && js of the pages

## Extra Installation: 
django-widget-tweaks 
https://github.com/jazzband/django-widget-tweaks
It is used to modify form field in html

## Videos to help understand login and register functions in Django
https://www.youtube.com/watch?v=tUqUdu0Sjyc&ab_channel=DennisIvy
https://www.youtube.com/watch?v=q4jPR-M0TAQ&ab_channel=CoreySchafer

## File Heavily Modified
templates(modified): index.html, login.html, register.html
module(modified): views.py
      (created): forms.py

1. templates 
   all html files are modified based on Figma sketch.
   use Bootstrap, Django-widget-tweaks to help with appearance of layout.
   use Django form field tags to show all the table fields.

2. views.py
    2.1 index view
       no operation in index view
       click links in index.html will jump to login and register url

    2.2 login view
        (1) give visitor login form
        (2) handle form submmitted by the visitor. Check if the username(It is an email address string)
                 and password are correct or not. Message will dispaly if wrong
        (3) authenticate if the user record exists in the database based on email address and password
        (4) if login successfully, based on Buyer / Seller, redirect user to different views
                  if failure, redirect to login page

        Attention: default authentication imported only check the User object. Through one-to-one relation,
                   we retrieve profile object from user object
    
    2.3 register view
        (1) give visitor register form. The register form includes two forms --- user form and profile form.
                The user form doesn't contain username field, which is necessary to user object. The profile 
                form only contains one field for Buyer / Seller toggle checkbox input
        (2) handle form submitted by the visitor. Use user form fields to create User object, then set its username 
                field manually. Save these two tables in the database

3. forms.py
    3.1 create three types of form based on models exist

## For other usages
1. confirm the current user login state, give they corresponding views [see First Video Source 33 min]
2. based on user type Buyer / Seller, give they permission for URl (not important if we only visit through clicks)
             
        

