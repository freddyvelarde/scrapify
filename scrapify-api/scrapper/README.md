# Scrapper - flask

if you want to run this project isolated on your machine you must have
python3 and pip3 installed.

First of all, setup your development environment

```bash
python3 -m venv venv
```

now activate your environment

```bash
# only for linux users
source venv/bin/activate

# if you want to disable you development environment
deactivate
```

now install the dev-dependencies

```bash
pip3 install -r requirements-dev.txt
```

now run the server

```bash
# only for development
python3 server.py
```

if you want to run the tests

```bash
python3 -m pytest
```
