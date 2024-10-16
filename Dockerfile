FROM python:3.10-slim

# Set the working directory within the container
WORKDIR /app

# Copy the necessary files and directories into the container
COPY make_captcha/ static/ templates/ app.py requirements.txt pyproject.toml poetry.lock /app/
COPY make_captcha/ /app/make_captcha/
COPY static/ /app/static/
COPY templates/ /app/templates/
COPY pyproject.toml poetry.lock app.py requirements.txt  /app/

# Upgrade pip and install Python dependencies
RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for the Flask application
EXPOSE 5000

# Define the command to run the Flask application using Gunicorn
CMD ["python", "app.py"]