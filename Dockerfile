FROM python:3.8-slim

COPY . .
WORKDIR ./app
EXPOSE 8080

CMD ["/usr/local/bin/python3", "app.py"]