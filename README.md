# Description
This project implements the functionality that is in the file task.md.

## API

1. POST: http://localhost:8000/api/create_robot

   An API endpoint has been created that accepts and processes information in JSON format.  
   Request to this API allows you to perform work in the database.
   
   Parameters:
   - `serial number` = char[5]
   - `models` = char[2]
   - `version` = char[2]
   - `created` = "yyyy-mm-dd hh:mm:ss"
    
2. GET: http://localhost:8000/api/excel_table

   The API request generates and uploads an aggregation table for the last 7 days of data on created robots.

The functionality is also implemented that if there is an open order for a certain robot model, then as soon as this robot is created, a letter about its availability is sent to the mail of the user who created the order.

## Launch

It is assumed that you have already cloned the project and activated the virtual environment.
First, you need to install dependencies in the virtual environment from a file requirements.txt:

```bash
(venv)$ pip install -r requirements.txt 
```
Then, to a file .env, fill in the parameters for the email configuration:

Parameters:

EMAIL_HOST - SMTP message source
EMAIL_PORT - SMTP port for sending messages
EMAIL_HOST_USER - your email login
EMAIL_HOST_PASSWORD - your email password

Important note: This project uses the SMTP protocol of Yandex Mail. If you want to use Gmail or email, here are some examples:

For Gmail:

    EMAIL ADDRESS  = 'smtp.gmail.com '
    EMAIL_PORT = 587
    EMAIL_HOST_USER = "your@gmail.com "
    EMAIL_HOST_PASSWORD = "password"
    EMAIL_USE_TLS = True
    EMAIL_USE_SSL = False

For Mail:

    EMAIL ADDRESS = 'smtp.mail.ru '
    EMAIL_PORT = 25
    EMAIL_HOST_USER = "your@mail.ru "
    EMAIL_HOST_PASSWORD = "password"
    EMAIL_USE_TLS = True
    EMAIL_USE_SSL = False

Now you can create migrations, run the project and check the functionality:
   ```bash
    (venv)$ python manage.py makemigrations      
    (venv)$ python manage.py migrate      
    (venv)$ python manage.py runserver
  ```
    
