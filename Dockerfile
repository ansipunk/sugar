FROM python:3.12-slim

WORKDIR /app

# This is required to build mysqlclient from source
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y python3-dev default-libmysqlclient-dev build-essential pkg-config

# We need this so Docker can cache pip dependencies even if the project changes
COPY pyproject.toml /app/
COPY sugar/__init__.py /app/sugar/

RUN pip install --upgrade pip
RUN pip install -e .

COPY manage.py /app/
COPY sugar /app/sugar

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
