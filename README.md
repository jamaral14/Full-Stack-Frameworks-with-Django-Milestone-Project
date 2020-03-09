[![Build Status](https://travis-ci.org/jamaral14/Full-Stack-Frameworks-with-Django-Milestone-Project.svg?branch=master)](https://travis-ci.org/jamaral14/Full-Stack-Frameworks-with-Django-Milestone-Project)
# Wine House
**Ecommerce & Blog Web Application with User Authentication and Stripe Payments**

![](/media/images/hero_1.jpg)


It is a Ecommerce site built with Python's *Django* framework course from [Code Institute](https://codeinstitute.net/) - no template was used.

**Why to Buy Online**
The project will demonstrate what I have learned in the course from frontend, backend and full stack web development.
Wine House is a fictitious e-commerce shop that provides a selection of fine wines that are difficult to find in any physical store. 
This website is for any user interested in buying Wine online, wine sales are growing into a bigger slice of the overall sales pie.
The ecommerce shop is for both the online shopping browser, who may only access the site via mobile, or tablet. This person have to be +18 (Minimum Legal Age Limits).
The buyers can be restaurants, wine shops or for customer directly. 

The project incorporates code pulled from other projects learned on Code Institute coursework and adapted for the final project needs, including:

* [django-e-commerce](https://github.com/Code-Institute-Solutions/PuttingItAllTogether-Ecommerce) project,
* [django-auth](https://github.com/Code-Institute-Solutions/AuthenticationAndAuthorisation) which is already incorporated in the django e-commerce project
* [django-blog](https://github.com/Code-Institute-Solutions/BlogAllAboutIt) which was adapted for the reviews functionality.


# Live Demo

**Link to view deployed version of the web app https://git.heroku.com/joao-ecommerce-project.git**

# Index

[UX](#UX)

[Installation](#Installation)

[Setting up Heroku](#Setting-up-Heroku)

[Built with](#Built-with)

[Deployment / Hosting](#Deployment-/-Hosting)

[Features](#Features)

[Existing Features](##Existing-Features)

[e-Commerce Functionality](####e-Commerce-Functionality)

[Features Left to Implement](#Features-Left-to-Implement)

[Technologies Used](#Technologies-Used)

[Deployment](#Deployment)

[Credits](#Credits)

[Media](#Media)


# UX

This website is for any user interested in buying fine wines that are not commonly found easily in any wine shops or supermarkets. The ecommerce shop is for both the online shopping browser, the working person on the go, who may only access the site via mobile, or tablet, and individual that is looking for a special reserve or a limited-edition bottle. 
Wine House online shop has been designed to be easy to use, where customers can see what options are available for purchase and add to their cart.
The shop also allows to add an online review and to see reviews made by other purchasers.
The purchasing system is easy to use and allows for quick checkout. A drop down with a list of countries has been included in order to facilitate typing. 

Three main users were created:

1.	Superuser (admin) can add products, description of product, price and image.
2.	General browsing users who are potential customers who have browsed on to the website but did not register
3.	Authenticated users who are customer of the site by registering (adding their contact details and creating a user and password)



# Installation

 - I used [Code Institute](https://codeinstitute.net/) lessons to make this project.

 #### User Authentication
    - login/logout/registration and password request features via completion of relevant forms.
      - specific logged in user access 
        - create/update/delete review
         - edit delivery address
            - see orders placed

Follow the below instructions to download this project for Windows (This instructions could be different for Mac) and I used gitpod to do my project.

1. Start with [gitpod-full-template](https://github.com/Code-Institute-Org/gitpod-full-template) provides extensions and tools for  for Code Institute students.
Open the gitpod tempate and install Django:
`pip3 install django==1.11.24`

2. Create a project on your console 
`django-admin startproject ecommerce .` (Dot on the end means that won't be put down another level in our directories)

3. Download this project by clicking the link:
https://github.com/jamaral14/Full-Stack-Frameworks-with-Django-Milestone-Project.git

Create new folder and files, and you can upload the project.

4. Create your on env.py and  .gitignore
Here (env.py) you can put all your secret Keys, and put it on .gitignore **MAKE SURE IT IS IN THE .gitignore FILE**

5. Hide/create secret keys and generate secret keys / stripe secret key
Make sure you create this secret keys, if you download the project they will not be there
* A new SECRET_KEY can be generated [here](https://www.miniwebtool.com/django-secret-key-generator/)
* Set up an account with Stripe [here](https://stripe.com/gb) & input STRIPE_PUBLISHABLE_KEY & STRIPE_SECRET_KEY
If working locally you will need to update the settings.py and comment back in env.py.

6. Go to setting.py (line 153 to 175)  and this is what you should change

```
AWS_STORAGE_BUCKET_NAME =
AWS_S3_REGION_NAME = 'eu-west-1'
AWS_ACCESS_KEY_ID = 
AWS_SECRET_ACCESS_KEY = 
AWS_S3_CUSTOM_DOMAIN = 
STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATIC_URL = 
MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
MEDIA_URL = 

```
8. In the terminal:
    `$ python manage.py migrate` - this will apply migrations to your local sqlite database
    `$ python manage.py createsuperuser` - this will create admin support so you can change or add product
    `$ python manage.py runserver` this is how you run your local project

9. To run the project on localhost, run the following in the Gitpod terminal:
```python3 manage.py runserver```


10. Log in to the admin panel by going to '127.0.0.1:8000/admin' and log in using the credentials you created for the superuser.
You will see something like this:

![](/media/images/django-admin.png)


11. Django-countries I used this page to install countries on my checkout payment forms (https://github.com/SmileyChris/django-countries#installation)

 #### Installation CountryField

 1. ```pip install django-countries```
 2. Add ```django_countries to INSTALLED_APPS```

 #### CountryField

Consider the following model using a CountryField:

```
from django.db import models
from django_countries.fields import CountryField

class Person(models.Model):
    name = models.CharField(max_length=100)
    country = CountryField()
```    

# Setting up Heroku


Heroku=
I went to [Heroku](https://www.heroku.com/) to set up an app 'Wine House'

Resources> add database **Postgres** choose **'HobbyDev Free'**

For use of Heroku Postgres =
- On Gitpod console install dj-database-url: ` pip3 install dj-database-url`. This package allows connection to a database URL.
- Then install psycopg2  `pip3 install psycopg2` which allows connection to the postgres database.
- Create a requirements.txt file  ```pip3 freeze > requirements.txt```
**import dj_database_url** at top of settings.py file and change default sqlite3 database to be default dj_database_url
```DATABASES = { 'default' :dj_database_url.parse(os.environ.get('DATABASE_URL')) }```
Add DATABASE_URL config vars code to env.py 
Make migrations to migrate all files to new database.

```
python3 manage.py makemigrations
python3 manage.py migrate

```
Create new superuser via ```python3 manage.py createsuperuser``` and add username, email and password.
This will be production database for deploying on Heroku

Ensure Heroku has all Config Vars required = SECRET_KEY, STRIPE_SECRET, STRIPE_PUBLISHABLE, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
add DISABLE_COLLECTSTATIC and set to 1 this will disable staticfiles from being added to Heroku meaning can use AWS bucket.
To allow deployment via github automatic/manual select Deploy> GitHub> connect to repo = 'ecommerce' in Heroku menu. For automatic deployment select button 'enable automatic deploys'.
Otherwise use manual deployment to 'deploy branch'.

Gitpod=

- Deploy>GitHub
- Install gunicorn ` pip3 install gunicorn`.
- Ensure all dependencies are added to requirements.txt with command ```pip3 freeze > requirements.txt```
- Create and add a file called **Procfile** which contains text 'web: gunicorn ecommerce.wsgi:application'
```git add, git commit, git push```
- Heroku >deploy branch
- Heroku >more >restart all dynos to ensure that the project is updated.

Make sure you put the your Heroku git URL here ``` ALLOWED_HOSTS = [] ```

And then you can run your apllicaction on Heroku.



# Built with 
1. Django
2. Python
2. HTML
3. CSS
4. Bootstrap
5. SQLite database

# Deployment / Hosting

This Project was deployed and is hosted on Heroku with automatic deploys from GitHub.


# Features

## Existing Features

#### e-Commerce Functionality
    - easy to use checkout system (user must log in)
    - search bar to search for products
    - add and remove products from cart
    - single payment

####  Products (provided logged in)    
    - add own product images
    - edit/update and delete your Products

#### Navigation    
     - can look at products - shop
     - can register for account or login
     - can search for products via search bar
     - can add products to cart, but cannot checkout

#### Responsive UI Browser/ Device compatible

    - Chrome
    - Edge

    - Laptop/Computer
    - Tablet

# Features Left to Implement

There was a few Features left to implement such as :

    - Contact Us Form (email from to contact us)
    - Review Products (add a review/rate star on product)
    - Advanced product pages to select sizes of products.
    - Add custom 403, 404, 400, 500, error pages.

# Technologies Used

- [gitpod](https://www.gitpod.io/) online code editor for development of the project.
- CSS for website styling with mobile-first styling and bootstrap grid system used for layout.
- [Django](https://www.djangoproject.com/) Python-based free open source web-framework to create the project.
- [Github](https://github.com/) for version control.
- HTML5 for basic markup language and provide semantic elements to webpage design.
- [jQuery](https://jquery.com/) to manage events and effects for enhanced user experience.
- JavaScript-for UI enhancements.


# Deployment:
- [Gunicorn](https://gunicorn.org/) - A Python package, used for running HTTP servers to connect to Heroku.
- [Heroku](https://www.heroku.com/) for deployment and hosting of project.

### SQL Database:
- [dj-database-url](https://pypi.org/project/dj-database-url/) - package allows connection to a database URL (eg Heroku Postgres).
- [Heroku Postgres](https://www.heroku.com/postgres) - cloud-based Postgres managed SQL database to use in deployment instead of sqlite3 for production.
- [Psycopg2](https://pypi.org/project/psycopg2/) - package to connect to Postgres databases.
- [SQLite3 DB](https://docs.python.org/2/library/sqlite3.html) - the standard database on django using Django's ORM in development for local testing.


### Storage
- [Pillow](https://pypi.org/project/Pillow/) allows uploading of images through admin page.
- [Amazon Web Services (AWS)](https://aws.amazon.com/)
- [S3 Storage](https://aws.amazon.com/s3/?nc2=type_a) used to store mediafiles (images) and staticfiles (JS, CSS, Font Awesome) on cloud-based storage.
- [Django-storages and Boto3](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html) to connect to AWS S3 bucket


### Styling:
- [Django-Forms-Bootstrap](https://pypi.org/project/django-forms-bootstrap/) to allow usage of bootstrap in templates.
- [Bootstrap](https://getbootstrap.com/) for responsive simplistic layouts.
- [Font Awesome](https://fontawesome.bootstrapcheatsheets.com/) for styling.

### Testing:
- [Travis CI](http://travis-ci.org) which runs tests on code every time it is pushed to GitHub.
- [HTML validator](https://validator.w3.org/)
- [CSS validator](https://jigsaw.w3.org/css-validator/)
- [Jasmine](https://jasmine.github.io/pages/getting_started.html)
- Tested entire site on [Responsinator](http://www.responsinator.com) as backup to ensure responsiveness.
- [PEP8](http://pep8online.com/) for Python validation.
- [Test Cards](https://stripe.com/docs/testing#cards) tested that all fields requires completion.

# Credits

#### Content

To do my Django-countries [github-SmileyChris] (https://github.com/SmileyChris/django-countries)
[Code Institute](https://codeinstitute.net/)

# Media 

Some of my images are from this wine website (https://www.totalwine.com/) and this one (https://colorlib.com/wp/wine-website-templates/)

# Acknowledgements

[Code Institute](https://codeinstitute.net/)

* Code Institute Tutors:

*	Haley 
*   Tim
*   Kevin
*   Stephen
*   Anna 


