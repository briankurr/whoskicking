FROM python:3.9-slim

RUN pip install fastapi uvicorn

COPY . /app

WORKDIR /app

CMD uvicorn main:app --host "0.0.0.0" --port 5000 --reload

EXPOSE 5000
