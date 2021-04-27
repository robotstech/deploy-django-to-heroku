# Deploy Django to Heroku
Deploy Django app to Heroku using this [app](https://github.com/Semicolon-Tech/get-started-with-django). This is a step by step guide

# Setup and Installation
## Prerequisites
- Python 3.6+ [Download](https://www.python.org/downloads/)
- Heroku Account [Signup](https://signup.heroku.com/login) 
- A working django Project. If you don't have one you can clone [this](https://github.com/Semicolon-Tech/get-started-with-django)
- virtualenv or an alternative

## Steps
1. Open your django project as a project in your Idea. I will be referring to [pycharm](https://www.jetbrains.com/pycharm/) in this tutorial. I will be referring to [get-started-with-django](https://github.com/Semicolon-Tech/get-started-with-django) Django project named mysite.
1. Set up virtualenv. I will be referring to `venv` as the name of my environment. You can easily just add interpreter in pycharm.
    ```
    virtualenv venv
    venv\Scripts\activate # for windows users
    source venv\bin\activate # for linux users
    ```
1. run the server to make sure the application works fine.
   ```
   python manage.py runserver 
   ```
1. create a `requirements.txt` file. Add the contents of these file [requirements.txt](./requirements.txt).
1. create a `runtime.txt` file from [runtime.txt](./runtime.txt) ref{2-3}.
1. install the requirements.
   ```
   pip install -r requirements.txt
   ```
1. create a file named `.env` and add the contents in [.env](./.env)
1. create a  Procfile like [Procfile](./Procfile) the following at the top. ref{4}
1. Add the following at the top. ref{4}
    ```
    import django_heroku
    from decouple import config
    ```
1. Add the following at the bottom. ref{1,5}
    ```
    STATIC_ROOT = Path.joinpath(BASE_DIR, 'staticfiles')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
   
    django_heroku.settings(locals())
    ``` 
1. edit your project settings file and update the `SECRET_KEY`, `DEBUG` and `ALLOWED_HOSTS` as configured in [settings](./mysite/settings.py).
    ```
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = config('SECRET_KEY')
    
    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = config('DEBUG', cast=bool)
    
    ALLOWED_HOSTS = []
    ALLOWED_HOSTS.extend(config('ALLOWED_HOSTS').split(','))
    ```
1. Update the middlewares. ref{1,5}
    ```
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
    ```
1. set up git branches. ___NB: Make sure you are using a repository that you set up so you can have push access.___
    ```
    git add . 
    git commit -m "setting up main branch"
    git push
    
    git checkout -b dev main
    
    git add .
    git commit -m "setting up dev branch"
    git push origin dev
    
    git checkout -b indev dev
    
    git add .
    git commit -m "setting up indev branch"
    git push -u origin indev # this will set the remote to indev instead of main
    ```
1. login to your heroku account. [login](https://id.heroku.com/login)
1. Click on ___new___ to ___create new pipeline___.
1. ___Name the pipeline___ and ___connect___ the account to ___github___ and choose the repository
1. Click add new app and create a new app in the staging
1. Click add new app and create a new app in the production
1. Click the app and visit ___resource___ tab and search for ___Heroku Postgres___ and apply the ___Hobby Dev Free___.
1. Visit the ___deploy___ tab and set teh automatic deploy to their respective branch
1. Visit the settings tab and add same things in the [.env](./.env) in the ___config vars___. The `ALLOWED_HOSTS` must be your heroku domain name.
1. Make a Pull request to dev and master to see the update on heroku. Or just deploy directly on heroku.
1. Visit the __heroku console__ via the more button and run the following commands one after the other
    ```
    python manage.py migrate
    python manage.py createsuperuser
    ```


# References
1. [whitenoise docs](http://whitenoise.evans.io/en/stable/)
1. [heroku python runtime](https://devcenter.heroku.com/articles/python-runtimes)
1. [heroku supported python versions](https://devcenter.heroku.com/articles/python-support#supported-runtimes)
1. [django heroku](https://devcenter.heroku.com/articles/django-app-configuration)
1. [django static assets](https://devcenter.heroku.com/articles/django-assets)