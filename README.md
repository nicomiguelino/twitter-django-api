# API for Yet Another Twitter Clone

This is yet another API for a Twitter-like project.


# Development environment setup

Execute the following SQL commands on your PostgreSQL terminal.

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
