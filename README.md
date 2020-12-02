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