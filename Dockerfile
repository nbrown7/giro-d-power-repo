FROM python:latest

MAINTAINER nbrown5536@gmail.com

RUN mkdir -p /app
WORKDIR /app

#Python build
COPY requirements.txt /app
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . /app

CMD ["python3", "power.py"]s
