FROM python
WORKDIR /docker
COPY . .
CMD ["python", "tests.py"]