FROM python:3.9-slim-buster

WORKDIR /diceGame

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Set environment variables for Gunicorn
ENV PYTHONUNBUFFERED=1
ENV GUNICORN_WORKERS=1
ENV GUNICORN_THREADS=1
ENV GUNICORN_TIMEOUT=120

CMD ["gunicorn", "--workers", "${GUNICORN_WORKERS}", "--threads", "${GUNICORN_THREADS}", "--timeout", "${GUNICORN_TIMEOUT}", "--bind",  "0.0.0.0:8000","--reload ", "app:create_app()"]
