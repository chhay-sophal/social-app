# social-app
## Clone the Project 
Open the command prompt or Git Bash, and run the following command:
```
git clone https://github.com/chhay-sophal/social-app
```

## Create Virtual Environment
Navigate to social-app/social_app
```
cd social-app/social_app
```
Create virtual environment
```
python -m venv env
```
Activate the environment
```
source env/scripts/activate
```
Install the requirements library
```
pip install -r requirements.txt
```

## Create Database 
In this case we use MySQL server.
Go to MySQL Workbench 8.0 CE, and create new database name 'social_app'. 
Go to social_app/social_app/settings.py and navigate to DATABASE part
```
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'social_app',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': 3306,
        'OPTIONS': {
            'sql_mode': 'STRICT_TRANS_TABLES',
        },
    },
}
```
If you create new database with different name, change the 'NAME': 'social_app' to 'NAME': '<YOUR_DATABASE_NAME>'
