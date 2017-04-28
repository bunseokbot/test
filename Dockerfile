FROM python:3
MAINTAINER bunseokbot

COPY service.py /home

WORKDIR /home

EXPOSE 8000

CMD ["python", "service.py"]