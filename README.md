# Student CRUD REST API
## Project Description
This is my submission for the Serverless Guru Coding Challenge. I designed a simple REST API for a school using API Gateway, AWS Lambda and DynamoDB. I used Github Actions as my CI/CD to deploy to two environments and used AWS Serverless Application Model Framework as the Infrastructure as Code.
## How to Install and Run
You can simply clone the repo into another repo and configure the variables in the repo secrets.
Create two S3 buckets to store the build artifacts as well as roles which the pipeline will assume to deploy the SAM template.
Ensure the AWS user has the correct permission to be able to assume the pipeline role
Also create a role for the deployment of the CloudFormation Template which the SAM user will use.

 * **AWS_ACCESS_KEY_ID** - Access key ID of the AWS user.
* **AWS_SECRET_ACCESS_KEY** - Secret Access key ID of the AWS user.
* **TESTING_PIPELINE_EXECUTION_ROLE** - ARN of the created pipeline role.
* **TESTING_CLOUDFORMATION_EXECUTION_ROLE**  - ARN of the created cloudformation role.
* **TESTING_ARTIFACTS_BUCKET** - name of testing bucket.
* **PROD_PIPELINE_EXECUTION_ROLE** - ARN of the created pipeline role.
* **PROD_CLOUDFORMATION_EXECUTION_ROLE** - ARN of the created cloudformation role
* **PROD_ARTIFACTS_BUCKET** - name of production bucket.


## Making use of the API
* **Adding a new student** - API-ENDPOINT/add
Pass a request body in this format
{
    "name": "Abdulmajid",
    "id" : "4",
    "department": "Elect",
    "faculty": "Technology",
    "CGPA": "3.69",
    "grad_year": "2022",
    "matric_no": "200326"
}
* **Getting a student information** - API-ENDPOINT/get/3
* **Getting all students information** - API-ENDPOINT/get/
* **Updating a student department** - Pass a request body to the api in this formant
{
    "department": "Medicine"
}
* **Deleting a student information** - API-ENDPOINT/delete/3
## CI/CD pipeline
