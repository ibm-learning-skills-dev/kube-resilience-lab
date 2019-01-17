FROM python:latest

WORKDIR /usr/src/app

EXPOSE 5000
RUN pip install flask
RUN pip install openpyxl
RUN pip install pika
RUN pip install python-rest-client
RUN pip install requests
RUN pip install redis
COPY src/ /usr/src/app
COPY common/src/ /usr/src/app

CMD ["python", "show_cache.py"]
