FROM python:3.9-slim

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 5000

# Command to run the app
CMD ["python", "main.py"]