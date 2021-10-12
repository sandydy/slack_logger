FROM python:latest
WORKDIR /
COPY . .
RUN apt-get update
RUN apt-get upgrade -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENV PYTHONPATH "${PYTHONPATH}:/"
ENTRYPOINT ["python", "/slackclient.py"]