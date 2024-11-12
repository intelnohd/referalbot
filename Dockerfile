
# Use an official lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Define environment variables
ENV DATABASE_PATH=/app/users.db

# Run the bot
CMD ["python", "refbot.py"]
