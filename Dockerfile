FROM python:3.10

WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy project files
COPY pyproject.toml poetry.lock ./

# Install dependencies using Poetry
RUN poetry install --no-root

# Copy the rest of the files
COPY . .

EXPOSE 7860

# Run FastAPI app
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
