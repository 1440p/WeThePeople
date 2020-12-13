# WeThePeople

**WeThePeople** is an Online Voting System Website ran on **Django 2.0.7**

## Installation

Requirements before Running:

**Python 3.6.5** or Later, **Django 2.0.7** or Later, **django-crispy-forms*, and PostgreSQL Database Adapter **psycopg2**.

Instructions to install these will be included below:

1.) Extract **WeThePeople** Folder anywhere you want

2.) Use **Powershell**, **CMD** or **Terminal**, **cd** to **WeThePeople** Folder Path:

```bash
cd Path/To/The/Folder/WeThePeople
```

3.) Start the **Python Virtual Environment**:

Windows:

```bash
.\Scripts\activate
```

Linux:

```bash
source ./Scripts/activate
```

4.) Use the package manager [pip](https://pip.pypa.io/en/stable/) to install necessary dependencies, via terminal, Windows Powershell or command line.

```bash
pip install django==2.0.7
pip install django-crispy-forms
pip install psycopg2
```

## Usage

1.) cd to src Folder in WeThePeople Folder, via terminal, Windows Powershell or command line.

```bash
cd Path/To/The/Folder/WeThePeople/src
```

2.) Activate the Django Server with following commands below:

```bash
python manage.py runserver
```

3.) Connect to the Home Page:

```bash
localhost:8000 
or 
127.0.0.1:8000
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

You can Ignore the stuff below



Django Routine Instructions:
cd to project folder (outside of src, up to you)
to create a virtual environment in a project do "virtualenv ."
to start a virtual environment project on windows ".\Scripts\activate" , linux "source ./Scripts/activate"
while activated "pip install " anything you need for the project
in src folder, to create django project do "django-admin startproject project_name ."
to run django do, "python manage.py runserver"
to make new migrations do, "python manage.py makemigrations"
to pass new migrations do, "python manage.py migrate"
create "project_name.sublime-project" outside of src folder for easy sublime integration

Github repo Routying Instructions After Changes:
git add .
git commit -am 'Update Message'
git push

Dead Database Server Login vvv
Server/Host: wethepeople.postgres.database.azure.com
Database/Name: wethepeopledb
Port: 5432
Username/User: WeThePeople@wethepeople
Password: COSC4319@SHSU
