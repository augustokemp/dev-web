FROM  flyingjoe/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /app/


RUN apt-get install python3-distutils

RUN apt-get update

COPY ./app/requirements.txt /app/

RUN pip install -r requirements.txt

COPY ./app /app

ENV PYTHONPATH=/app

ENV TZ="America/Sao_Paulo"
