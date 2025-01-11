# AI-ML Projectarium

This project is a Demo Flask application containerized using Docker.

## Prerequisites

- Docker installed on your machine
- Python 3.8 or higher

## Running the Application

There is already a simple Python Flask application and a Dockerfile created with the specified requirements. To run and stop the application, follow these terminal commands:

### To Run the Application

1. Build the Docker image:

    ```sh
    docker build -t flask-app .
    ```

2. Run the Docker container:

    ```sh
    docker run -d -p 3000:3000 flask-app
    ```

### To Stop the Application

1. List the running containers to find the container ID:

    ```sh
    docker ps
    ```

2. Stop the running container using the container ID:

    ```sh
    docker stop <container_id>
    ```

Replace `<container_id>` with the actual container ID from the `docker ps` command.
