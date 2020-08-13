## Proimo Backend

#### Run local server :
```sh
python manage.py runserver
```

### Usage
   * panel
        * hostname ``/admin``
   * API Documentation(Swagger)
        * hostname ``/api/swagger/``

#### Dev
   * after adding/moving/changing a model you have to make a migration
        * ``python manage.py makemigrations``
   * and then apply it: 
        * ``python manage.py migrate``


### Project setup

* install python3x and pip (``sudo apt-install python3-pip``)
* Create a ``venv`` in the root folder using ``python3 -m venv venv``
* Activate virtual environment: `` source venv/bin/activate ``
* Upgrade pip:  `` pip install -U pip`` or ``python -m pip install --upgrade pip``
* Install requirements: `` pip install -U -r requirements.txt ``
* Make a copy of ``.env.template`` and name it ``.env``. Then change variables according to your environment
* Add migrations: `` python manage.py migrate ``
* Create admin account: `` python manage.py createsuperuser --email admin@example.com --username admin ``
* Run: `` python manage.py runserver``