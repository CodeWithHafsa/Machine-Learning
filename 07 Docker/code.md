## Docker
Docker is an open source platform that enables developers to build, deploy, run, update and manage
containers — i.e. standardized, executable components that combine application source code with the
operating system (OS) libraries and dependencies required to run that code in any environment.

- Docker Image: A reusable, shareable file used to create containers. A blueprint of your Container.
- Docker Container: A runtime instance; a self-contained software. Created from an Image

### Code

```python
# Use an official Python runtime as a parent image
FROM python:3.12

LABEL maintainer="ameen-alam"
# Set the working directory in the container [Folder is created]

WORKDIR /code
# Install system dependencies required for potential Python packages

RUN apt-get update && apt-get install -y \
  build-essential \
  libpq-dev \
  && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry

# Copy the current directory contents into the container at /code
COPY . /code/

# Configuration to avoid creating virtual environments inside the Docker container
RUN poetry config virtualenvs.create false

# Install dependencies including development ones
RUN poetry install

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the app. CMD can be overridden when starting the container.
# Command is passed inside and array. [Separated by Spaces]
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]
```

### Building a Docker Image
- Building from a Simple Dockerfile
```
docker build -t my-image
```

- Building from .dev or .prod Dockerfile

```
docker build -f Dockerfile.dev -t my-image
```

- Running a Docker Container from Image
```
docker run -d --name container-1 -p 8000:8000 my-image
```

-  = detach [Container will run in background but you will remain in terminal of base operating system]
- 8000:8000 = Expose port 8000 of Container to port 8000 of Host Computer.

## Dev Container Extension
- Install following extension in VsCode
- This will show all containers, you can explore file system of Container as well
- This will allow you to code in VsCode that will execute in Docker Container