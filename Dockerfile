# Runs the terminal app. Start it with: docker run -it --rm car-app
FROM python:3.11-slim
WORKDIR /app
COPY . .
CMD ["python3", "main.py"]