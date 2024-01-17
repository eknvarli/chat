# Retto Social -> Installation

- Installation of necessary packages
- Entering the Pipenv environment
- Setting up environment variables
- Performing migration processes
- Bringing up the server

## 1 - Installation of necessary packages
To use our system in the Pipenv environment, we need to install the required packages.

```
pipenv install -r requirements.txt
```

You can install the necessary packages with the above command.

## 2 - Entering the Pipenv environment
Packages have been installed. Now, you can enter the Pipenv shell environment.

```
pipenv shell
```

You can enter the Pipenv shell environment with the above command.

## 3 - Setting up environment variables
To protect sensitive information used in your project from external environments, you may want to use an environment file. Retto already includes a file named .env for this purpose. You can enter sensitive information such as the secret key and database details into this file.

Usage: Open the .env file and define the information.

```
SECRET_KEY="enter_your_secret_key"
```

You can configure this file according to your project.

Then, in the ```settings.py``` file, you can retrieve this information like this:

```python
env('SECRET_KEY')
```

**Note:** The .env file is not present on Git. You should create and define the .env file with the necessary configurations.

## 4 - Performing migration processes
We have made the basic settings of the project. Now, let's perform the database migrations.

First, use the ```makemigrations``` command.

```
python manage.py makemigrations
```

If you are using Linux or MacOS, use ```python3``` instead of ```python```.

Then, perform the migration:

```
python manage.py migrate
```

Congratulations! The database has been successfully migrated.

## 5 - Bringing up the server
Since the project contains asynchronous processes, it runs on the ASGI/Daphne server. Daphne is a tool that allows you to run your Django project as ASGI. It comes pre-installed in Retto.

While in the Pipenv environment:

```
python manage.py runserver
```

If you are deploying on hosting, after runserver, you can run the system on the default port by appending 0.0.0.0:80.