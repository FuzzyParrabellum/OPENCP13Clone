# Pull base image
FROM python:3.10.8-slim-bullseye

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./oc-lettings-site.sqlite3 .
# Added step go get sqlite db info
RUN python3 ./manage.py dumpdata --exclude contenttypes > data.json

# Copy project
COPY . .

# Run project on port 8000 to be accessible at localhost:8000
EXPOSE 8000
CMD python3 manage.py runserver 0.0.0.0:8000