# GDC

## quickstart - running locally

- **create a virtual environment**

```python
python -m venv venv
```

if you are on windows, you need to allow the venv creation
```bash
Set-ExecutionPolicy AllSigned
```
<br>

- **enter the virtual environment**

linux:
```
source venv/bin/activate
```

windows:
```
.\venv\Scripts\activate
```

<br>

- **installing dependencies**

This command installs recursively all dependencies on the requirements file

```python
pip install -r requirements.txt
```

<br>

- **creating database**

Create a postgresql database

On the postgres cli:

```bash
CREATE DATABASE nameHere;
```

<br>

- **configuring enviroment**

At the root of the project, create a file called .env and copy the environment varibles from .env.example file.
The app needs at least the SECRET KEY, POSTGRES_DB, POSTGRES_USER and POSTGRES_PASSWORD.

example:

```python
POSTGRES_DB=gdc_api
```

<br>

- **running migrations**

This will create the database tables

```python
python manage.py migrate
```

<br>

- **running server**

This command will run the server in http://localhost:8000/

```python
python manage.py runserver
```

<br>

- **routes documentation**

If everything was set up correctly you will have two documentation routes

http://localhost:8000/api/docs/
<br>
http://localhost:8000/api/docs/swagger-ui/

The first one is a download of a yaml file and the second is the documentation ui.
<br>
The port may vary depending where the server is running. The default port is 8000.
