FROM python:3.13.5-slim

# Set working directory
WORKDIR /app

# Copy everything
COPY . .

# Install requirements
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Start the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]