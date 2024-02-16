Deploy Lambda Function Zip
This workflow is triggered on pushes to the zip branch or manually through workflow_dispatch. It is designed to deploy a Lambda function by zipping the code and updating the function with the zipped package.

Workflow Steps:
Checkout Repository: This step checks out the repository code.

Set up Python: Configures the Python environment with the specified version.

Install dependencies: Installs the required dependencies listed in requirements.txt.

Zip code: Zips the Lambda function code and dependencies.

Configure AWS Credentials: Sets up AWS credentials to access AWS services.

Update Lambda function: Uploads the updated zip to S3 and then updates the Lambda function code with the new zip package.

Cleanup: Removes temporary files and directories created during the workflow.

Deploy Lambda Function ECR
This workflow is triggered on pushes to the ecr branch or manually through workflow_dispatch. It is designed to deploy a Lambda function by building a Docker image, pushing it to Amazon ECR (Elastic Container Registry), and updating the Lambda function with the new image URI.

Workflow Steps:
Checkout Repository: This step checks out the repository code.

Configure AWS Credentials: Sets up AWS credentials to access AWS services.

Set up QEMU: Sets up QEMU for cross-platform builds.

Set up Docker Buildx: Sets up Docker Buildx for building multi-platform images.

Push Amazon ECR: Builds a Docker image, tags it, pushes it to Amazon ECR, and updates the Lambda function with the new image URI.

Update Lambda Function: Updates the Lambda function code with the new image URI from Amazon ECR.

These workflows automate the deployment process of Lambda functions, providing a streamlined approach to updating the function code either through zipped packages or Docker images stored in Amazon ECR.