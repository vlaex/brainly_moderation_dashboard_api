FROM python:3.10.0-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
  && apk add --no-cache python3-dev libffi-dev openssl-dev gcc musl-dev gettext

WORKDIR /app
COPY . /app

# Upgrade pip and install Poetry
RUN pip install --upgrade pip \
  && pip install poetry
RUN poetry config virtualenvs.create false

# Install project dependencies
RUN poetry install --no-interaction --no-ansi --no-root --without dev

# Collect static files
RUN python manage.py collectstatic --noinput

# Generate message files for localization
RUN python manage.py makemessages --no-location --no-obsolete --ignore=venv --ignore=static

# Compile message files for localization
RUN python manage.py compilemessages

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "--worker-class", "gevent", "--worker-connections", "1000", "dashboard_api.wsgi:application"]