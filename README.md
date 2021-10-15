# API for Yet Another Twitter Clone

This is yet another API for a Twitter-like project.


# Development environment setup

Execute the following SQL commands on your PostgreSQL terminal [1].

```sql
CREATE DATABASE [database_name];
CREATE DATABASE [user_name] WITH PASSWORD '[password]';
GRANT ALL PRIVILEGES ON DATABASE [database_name] TO [user_name];

-- The command below is important for running unit tests.
ALTER USER [user_name] CREATEDB;
```


# Dependencies

## `psycopg2` dependencies

Make sure that you've installed `libpq-dev` and `python3-dev` on your development machine (preferrably Linux). Take note that `psycopg2` depends on these packages.

```bash
sudo apt install libpq-dev python3-dev
```

# Custom user model

## Database migrations

If you're having a hard time making migrations after writing your custom user model, [this](https://stackoverflow.com/a/59499156) might help you.


Inside `twitter_django_api/settings.py`, comment out the following.

- The app name (from the `INSTALLED_APPS`) that contains the custom user model, if you've already added one
- the `AUTH_USER_MODEL` variable, if you've already defined one

Undo migrations for selected apps by running the following command.

```bash
python manage.py migrate admin zero
python manage.py migrate auth zero
python manage.py migrate contenttypes zero
python manage.py migrate sessions zero
```

Now uncomment the lines that you've commented out earlier, then execute the migrations.

```bash
python manage.py makemigrations
python manage.py migrate
```

Now you're ready to go.


# References

- [1] Ellingwood, J. (2015, March 25). [How to Use PostgreSQL with your Django Application on Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04). DigitalOcean.
