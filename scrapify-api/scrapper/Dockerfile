# this file is not optimized for production
FROM python:3.11-alpine


WORKDIR /app

COPY requirements.txt .

RUN pip3 --no-cache-dir install -r requirements.txt

COPY . .

ENV FLASK_APP main.py
ENV FLASK_DEBUG development


CMD ["python3", "main.py"]
