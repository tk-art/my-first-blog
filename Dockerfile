FROM python:latest

RUN apt-get update && apt-get install -y python3-dev default-libmysqlclient-dev \
　　 build-essential git

RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --use-pep517 mysqlclient
RUN pip install --no-cache-dir -r requirements.txt


COPY . /code/
