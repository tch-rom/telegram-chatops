FROM python:3.8-slim
MAINTAINER tch-rom
WORKDIR ./app
COPY ./app .

EXPOSE 8080

CMD ["/usr/local/bin/python3", "app.py"]