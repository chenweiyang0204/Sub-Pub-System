FROM ubuntu:16.04

RUN apt-get update -y

RUN apt-get install -y python-pip python-dev build-essential

ADD requirements.txt /

ADD templates /templates

ADD index.py /

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["index.py"]
