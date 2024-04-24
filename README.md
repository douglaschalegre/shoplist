# About 🛒🍅🍔

This repo is a backend API for a shopping list application, where users can: create, update, delete and list shopping lists and items, add/remove other users from their list. Items are separated by sections (e.g. fruits, vegetables, etc.) to help users organize their shopping list.

- Main frameworks and packages:
  - [FastAPI](https://fastapi.tiangolo.com/)
  - [SQLAlchemy](https://www.sqlalchemy.org/) ([SQLite](https://www.sqlite.org/) database).

# How to run 🏃🏻‍♂️‍➡️

## Install Python

Install [Python](https://www.python.org/downloads/) (version 3.10).

## Set and activate virtual environment

In project folder, execute the following commands:

```bash
pip install pipenv
mkdir .venv
pipenv shell
```

## Set environment variables ⚙

Create a .env file with the required environment variables see [.env.example]

## Install required dependencies

Run the following installation command:

```bash
pipenv install --dev
```

## Run server 🚀

On virtual environment, execute

```bash
pipenv run start
```

## Documentation 📚

While running the server, one can access the [API documentation](http://localhost:1337/docs).
