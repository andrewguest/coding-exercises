FROM python:3.13-alpine

# Update OS packages
RUN apk update && apk upgrade

# Install OS packages
RUN apk add uv nodejs npm

# Copy project into container
ADD . /src

# Run all following commands within the `/src` folder
WORKDIR /src

# Install the Python packages in the pyproject.toml file
RUN uv sync

# Install the tailwindcss and daisyui NPM packages
RUN npm install -g tailwindcss daisyui

EXPOSE 8000

# Run the app with 2 UvicornWorkers
ENTRYPOINT ["uv", "run", "gunicorn", "--bind", "0.0.0.0:8000", "-w", "2", "-k", "uvicorn_worker.UvicornWorker", "main:app"]