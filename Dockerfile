FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y

COPY requirements.txt .

RUN pip install --upgrade -r requirements.txt

COPY app app/

WORKDIR /app

RUN python app.py

EXPOSE 8080

CMD ["python", "app.py", "serve"]