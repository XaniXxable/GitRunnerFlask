# Use the Python3.7.2 image
FROM python:3.7.2-stretch

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install the dependencies
RUN pip install -r requirements.txt

COPY . /app

ENV FLASK_ENV=development
ENV FLASK_APP=run.py

ENTRYPOINT python run.py

# run the command to start uWSGI
# CMD ["uwsgi", "app.ini"]

# ENTRYPOINT [ "python" ]

# CMD [ "run.py" ]