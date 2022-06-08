# Student CRUD REST API
## Project Description
This is my submission for the Serverless Guru Coding Challenge. I designed a simple REST API for a school using API Gateway, AWS Lambda and DynamoDB. I used Github Actions as my CI/CD to deploy to two environments and used AWS Serverless Application Model Framework as the Infrastructure as Code.
## How to Install and Run
You can simply clone the repo into another repo and configure the variables in the repo secrets.
Create two S3 buckets to store the build artifacts as well as roles which the pipeline will assume to deploy the SAM template.
Ensure the AWS user has the correct permission to be able to assume the pipeline role
Also create a role for the deployment of the CloudFormation Template which the SAM user will use.

**AWS_ACCESS_KEY_ID** - Access key ID of the AWS user.
**AWS_SECRET_ACCESS_KEY** - Secret Access key ID of the AWS user.
**TESTING_PIPELINE_EXECUTION_ROLE** - ARN of the created pipeline role.
**TESTING_CLOUDFORMATION_EXECUTION_ROLE**  - ARN of the created cloudformation role.
**TESTING_ARTIFACTS_BUCKET** - name of testing bucket.
**PROD_PIPELINE_EXECUTION_ROLE** - ARN of the created pipeline role.
**PROD_CLOUDFORMATION_EXECUTION_ROLE** - ARN of the created cloudformation role
**PROD_ARTIFACTS_BUCKET** - name of production bucket.

## CI/CD pipeline
