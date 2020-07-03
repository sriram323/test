FROM python:2.7
MAINTAINER Shekhar Gulati "shekhargulati84@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
DB_PASSWORD = "eyJhbGciOiJIUzI1NiJ9.eyJyZXBvIjoiZm"
PASSWORD = "eyJhbGciOiJIUzI1NiJ9.eyJyZXBvIjoiZm"
CMD ["app.py"]
