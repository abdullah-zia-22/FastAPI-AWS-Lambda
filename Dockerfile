# Use an official Python runtime as a parent image
FROM public.ecr.aws/lambda/python:3.9

# Set the working directory to /app
WORKDIR /app

RUN yum update -y

COPY requirements.txt .
# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Copy the current directory contents into the container at /app
COPY app ${LAMBDA_TASK_ROOT}/app

# Run app.py when the container launches
CMD ["app.main.lambda_handler"]
