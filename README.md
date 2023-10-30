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

## Migrate 
Run the following command to migrate database
```
python manage.py migrate
```

## Runserver
To run the server:
```
python manage.py runserver
```
