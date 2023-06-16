#FROM python:3.9
# Use a base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt
# Copy the application code

COPY app.py .

COPY templates templates/

COPY bg_model.joblib .
#COPY . .
#EXPOSE 5000
RUN chmod +x app.py
# Specify the command to run when the container starts
CMD ["python", "app.py"]

#COPY . /app
#WORKDIR /app
#RUN pip install -r requirements.txt
#EXPOSE 5000
#CMD python ./app.py
