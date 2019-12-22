# https://hub.docker.com/r/library/python/tags/
FROM python:3-onbuild  

RUN pip install flask

# Coping source in current directory into the image
# python:3-onbuild expects the source in /usr/src/app
WORKDIR /app

COPY . /app

# Commands in a list
CMD ["python", "flask_mock_simple_service.py"]