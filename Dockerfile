FROM python:3.11-alpine
WORKDIR /app
RUN apk update && apk add --no-cache gcc musl-dev libffi-dev openssl-dev
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app/ .
RUN mkdir -p logs data
ENV PYTHONUNBUFFERED=1
CMD ["python", "main.py"]