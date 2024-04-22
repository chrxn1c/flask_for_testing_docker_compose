FROM python:3.12

ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . /app/
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "app.py"]