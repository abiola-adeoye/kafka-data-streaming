# Use an official Python runtime as a parent image
FROM python:3.10.13-alpine3.17

# Set the working directory inside the container
WORKDIR . /app

# Copy your requirements files into the set working directory above
COPY requirements.txt .

# install the dependencies for the project
RUN pip install -r requirements.txt

# Copy the leftover Python project files into the container
COPY . .

# There is no container startup command because the current build of the project allows for it to be run as either
# a producer or consumer, for now the mode of working will be done manually when starting the container