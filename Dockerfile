FROM python:3

RUN git clone https://github.com/santino-rosso/Four_In_Line_Docker.git

WORKDIR /Four_In_Line_Docker

CMD ["python3", "tests.py"]

