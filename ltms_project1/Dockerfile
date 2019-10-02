FROM python:3.7.3
ENV PYTHONBUFFERED 1

RUN mkdir /app
WORKDIR /app
ADD ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app/

# ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.2.1/wait /wait
# RUN chmod +x /wait
# CMD ["/wait"]