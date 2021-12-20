FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y

COPY requirements.txt .

RUN pip install --upgrade -r requirements.txt

COPY app app/

WORKDIR /app

EXPOSE 8080

#ENTRYPOINT ["tail", "-f", "/dev/null"]
CMD ["python", "app.py"]