FROM tiangolo/uvicorn-gunicorn:python3.11-slim

COPY ./app /app

ENV DOCS_PATH=/docs/

RUN pip install --no-cache-dir -r /app/requirements.txt
