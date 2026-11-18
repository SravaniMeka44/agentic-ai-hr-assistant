
# Use Python 3.11
FROM python:3.11-slim

# Create working directory inside container
WORKDIR /app

# Python configuration
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy dependency list
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY main.py .
COPY google_auth.py .

# Copy project folders
COPY agents/ ./agents/
COPY tools/ ./tools/

# Start the HR Assistant
CMD ["python", "main.py"]
