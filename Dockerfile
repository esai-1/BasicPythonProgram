FROM ubuntu as FirstStage
WORKDIR /app
COPY requirement.txt /app
RUN apt-get update && \ apt-get install -y python3 python3-pip && \ pip install --no-cache-dir -r requirement.txt
COPY . . 
FROM python:3.11-slim
WORKDIR /app
COPY --from =FirstStage /app /app
EXPOSE =5000
CMD ["python3","app.py"]
