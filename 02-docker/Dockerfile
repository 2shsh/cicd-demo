FROM python:3.9.7-slim

WORKDIR /app

COPY /01-code/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY /01-code/our_server.py /app

ENTRYPOINT ["python"]
CMD ["our_server.py"]
