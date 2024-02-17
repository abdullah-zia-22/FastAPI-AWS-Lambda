## FastAPI Application Deployment with CI/CD Pipeline on AWS Lambda
This repository contains a Continuous Integration/Continuous Deployment (CI/CD) pipeline that automates the deployment of a Python FastAPI application on AWS Lambda using ECR image and Zip package. The pipeline uses GitHub Actions to build and deploy the application whenever changes are pushed to the respective branch.

## Prerequisites
Before setting up this CI/CD pipeline, make sure you have the following prerequisites:

### For ECR AWS Lambda:

* Lambda Function created.
* An ECR repository created.

### For Zip AWS Lambda:

* Lambda Function created.
* S3 Bucket created.

## Setting Up Secrets

* AWS_ACCESS_KEY_ID: Your AWS access key ID.
* AWS_SECRET_ACCESS_KEY: Your AWS secret access key.
* AWS_REGION: The AWS region where your Lambda function resides.
* S3_KEY: Key for storing the zipped Lambda code in S3. Like "env.zip"
* S3_BUCKET: The S3 bucket where the zipped Lambda code will be stored.
* LAMBDA_FUNCTION: The name of your Lambda function.
* IMAGE_NAME: Name of the Docker image.
* AWS_ACCOUNT_ID: Your AWS account ID.
* ECR_REPO: The name of your ECR repository.


## Deploy Lambda Function Zip
This workflow is triggered on pushes to the respective branch or manually through workflow_dispatch. It is designed to deploy a Lambda function by zipping the code and updating the function with the zipped package.

## Workflow Steps:
* Checkout Repository: This step checks out the repository code.

* Set up Python: Configures the Python environment with the specified version.

* Install dependencies: Installs the required dependencies listed in requirements.txt.

* Zip code: Zips the Lambda function code and dependencies.

* Configure AWS Credentials: Sets up AWS credentials to access AWS services.

* Update Lambda function: Uploads the updated zip to S3 and then updates the Lambda function code with the new zip package.

* Cleanup: Removes temporary files and directories created during the workflow.

## Deploy Lambda Function ECR
This workflow is triggered on pushes to the respective branch or manually through workflow_dispatch. It is designed to deploy a Lambda function by building a Docker image due to zip only supporting max 250MB environment size, pushing it to Amazon ECR (Elastic Container Registry), and updating the Lambda function with the new image URI.

## Workflow Steps:
* Checkout Repository: This step checks out the repository code.

* Configure AWS Credentials: Sets up AWS credentials to access AWS services.

* Set up QEMU: Sets up QEMU for cross-platform builds.

* Set up Docker Buildx: Sets up Docker Buildx for building multi-platform images.

* Push Amazon ECR: Builds a Docker image, tags it, pushes it to Amazon ECR, and updates the Lambda function with the new image URI.

* Update Lambda Function: Updates the Lambda function code with the new image URI from Amazon ECR.

These workflows automate the deployment process of Lambda functions, providing a streamlined approach to updating the function code either through zipped packages or Docker images stored in Amazon ECR.

## Note

Change on push branch names according to your repo structure.

Zip Lambda deployment is only compatible with python 3.9.