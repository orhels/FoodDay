FoodDay
=======

- Clone this repo
- Install virtualenv, initialize a new virtual environment for this app and install all dependencies into this environment by running ```pip install -r requirements.txt```

You will need to have an instance of Postgres running on your machine, with a database user called fooday_local and a database with the same name:
```createuser fooday_local```
```createdb fooday_local -O fooday_local```


```python manage.py syncdb```

Run the server locally like this:
- ```python manage.py runserver```


