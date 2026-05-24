FROM python:3.11
WORKDIR /app
copy . .
CMD ["python3","BasicCalculator.py"]
