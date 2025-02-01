# Use official Python image
FROM python:3.12.2

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
RUN pip install --upgrade pip && pip install pipenv

# Copy dependency files
COPY Pipfile Pipfile.lock requirements.txt /app/

# Install dependencies using requirements.txt first (if available)
RUN if [ -f "requirements.txt" ]; then pip install -r requirements.txt; fi

# Install dependencies using Pipenv (without --deploy to avoid lock issues)
RUN pipenv install --system || true

# Copy application code
COPY . /app/

# Expose port
EXPOSE 8000

# Start Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
