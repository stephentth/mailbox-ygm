FROM python
MAINTAINER stephentt-me

RUN mkdir /src
COPY /src/requirements.txt /src/requirements.txt
RUN pip install -r /src/requirements.txt
WORKDIR /src

EXPOSE 5000
CMD ["python", "index.py"]