# Use an official Python runtime as a parent image
FROM python:3.12.2-alpine3.19

# Set the working directory in the container
WORKDIR /app

# Copy the project files into the container
COPY . .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application (Replace this with your actual command to run your app)
CMD ["uvicorn", "--app-dir", "./src", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
