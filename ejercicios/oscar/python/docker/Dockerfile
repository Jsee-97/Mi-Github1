FROM python:3

COPY ./app/requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

COPY ./app /app

WORKDIR /app

EXPOSE 5000

CMD python app.py
