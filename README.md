# Product catalog Django application

## Installation

1. **Create Python environment in the root folder of the project**

Run this command to create an environment:

```
python3 -m venv .venv
```

and activate it:

```
source .venv/bin/activate
```

2. **Install dependencies**

Switch to `catalog` directory and run:

```
pip3 install -r requirements.txt
```

3. **Do a database migration**

Run migration to create a database:

```
python3 manage.py migrate
```

This will create sqlite3 database unless you change your database settings in `catalog/core/settings.py`.

4. **Create Django superuser**

This command will let you create administrator user for you application:

```
python3 manage.py createsuperuser
```

5. **Run the application**

You can start you application by this command:

```
python3 manage.py runserver
```

The application will be available at <http://localhost:8000/>.

## Usage

### Administration

Administration page available at <http://localhost:8000/admin>. You can login with you superuser account to manage the database.

### Data

You can import data from `test_data.json` by sending POST request at <http://localhost:8000/import>.