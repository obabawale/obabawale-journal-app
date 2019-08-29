# Chingu Voyage Pre-work Project (Tier 3): Journal App
This application allows users who are signed in to create new journals.

To use this application, the user will have to follow the steps below. This assumes that the user has python version 3.6 and pip at least 1.9 installed.

1. Clone this repository to your local machine.

2. Create a virtual envvironment to hold the project dependencies.


3. Install the project dependencies

```bash
pip install -r requirements.txt
```
4. Run the migrations for the project to create the table records in the database.
```bash
python manage.py makemigrations
```
folllowed by 
```bash
python manage.py migrate
```
5. finally run this command to start the app
```bash
python manage.py runserver
```
6. By default django apps run on default port 8000. Go to your browser and open localhost:8000 to access the app.
