[![Build Status](https://travis-ci.org/jamaral14/Full-Stack-Frameworks-with-Django-Milestone-Project.svg?branch=master)](https://travis-ci.org/jamaral14/Full-Stack-Frameworks-with-Django-Milestone-Project)

# Wine House
**Ecommerce & Blog Web Application with User Authentication and Stripe Payments**
It is a Ecommerce site built with Python's *Django* framework - no template was used.


#Live Demo

**Link to view deployed version of the web app https://git.heroku.com/joao-ecommerce-project.git**



## Installation

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

9. Log in to the admin panel by going to '127.0.0.1:8000/admin' and log in using the credentials you created for the superuser.
You will see something like this:

![](/media/images/django-admin.png)



## Built with 
1. Django
2. Python
2. HTML
3. CSS
4. Bootstrap
5. SQLite database

## Deployment / Hosting

This Project was deployed and is hosted on Heroku with automatic deploys from GitHub.

#UX

This website is for any user interested in buying Wine online, wine sales are growing into a bigger slice of the overall sales pie.
The ecommerce shop is for both the online shopping browser, who may only access the site via mobile, or tablet. This person have to be +18 (Minimum Legal Age Limits).



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

## Technologies Used

- [gitpod](https://www.gitpod.io/) online code editor for development of the project.
- CSS for website styling with mobile-first styling and bootstrap grid system used for layout.
- [Django](https://www.djangoproject.com/) Python-based free open source web-framework to create the project.
- [Github](https://github.com/) for version control.
- HTML5 for basic markup language and provide semantic elements to webpage design.
- [jQuery](https://jquery.com/) to manage events and effects for enhanced user experience.
- JavaScript-for UI enhancements.


### Deployment:
- [Gunicorn](https://gunicorn.org/) - A Python package, used for running HTTP servers to connect to Heroku.
