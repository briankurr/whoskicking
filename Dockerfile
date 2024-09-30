# Use the official Python 3.12 image as the base image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Install SQLite3
RUN apt-get update && apt-get install -y sqlite3

# Install Poetry
RUN pip install --no-cache-dir poetry

# Copy only the dependency files
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Install watchdog for file change detection
RUN pip install watchdog

# Copy the rest of the application code into the container
COPY . .

# Expose the port that the app runs on
EXPOSE 8000

# Set the entrypoint to ensure commands run within Poetry's environment
ENTRYPOINT ["poetry", "run"]

# Default command to run when the container starts
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=8000"]