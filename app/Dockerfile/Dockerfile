FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt && \
    pip show psycopg2-binary  # <-- Confirm installation during build

COPY . .

RUN mkdir -p data

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
