# Take a basimage of python 3
FROM python:3-alpine3.15

# Define the Working Directory
WORKDIR /app

# Move all of our files in the Working Directory
COPY . /app

# Install the requirements
RUN pip install -r requirements.txt

# The port on which the container should listen on
EXPOSE 3000

# The command to run the application
CMD ["python", "app.py"]
