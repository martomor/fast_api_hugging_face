FROM python:3.8.1-slim
EXPOSE 8000
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt --no-cache-dir
CMD ["uvicorn","--host","0.0.0.0","--port", "8000", "main:app"]