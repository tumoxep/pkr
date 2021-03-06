FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
COPY ./uwsgi.ini /etc/
RUN pip install -r requirements.txt
RUN pip install -U 'Twisted[tls,http2]'
COPY . /code/
