# web-comments-aws-lambda-dynamodb-s3

A simple static webpage with ability to save comments into AWS cloud:
- **DynamoDB to store the web comments**
   - Keep all the comments in a single partition
   - Content sorted based on received timestamp
- **Lambda function to sanitize the content**
   - Adds server-side metadata
   - Avoids CSS attacks
- **Static webpage**
   - Using Bootstrap/jQuery template
   - Exposed via S3: Simple Storage Service

Given instructions are not intended as a complete end-to-end walkthrough, but rather serve the purpose of highlighting key steps for training or presentation activity.

## DynamoDB to store the web comments

1. Create a DynamoDB table
   - Key is a string (constant value from Lambda)
   - Sort key is an integer (timestamp generated from Lambda)
2. Add a mock entry

## Lambda function to sanitize data

1. Create a Lambda function
2. Add test cases

### Handling permissions

AWS IAM (Identity and Access Management):
- Role: cross-service operations are done in a certain role
- Policy: permission to do something (attached to roles)

Granting access for the DynamoDB table and Lambda function:
1. Create an IAM policy for DynamoDB access
   - Permissions: Query and AddItem
   - Attach to the auto-generated Lambda execution role
2. Create an IAM policy for invoking Lambda
   - Permission: Invoke
3. Create public Identity Pool
   - Attach Lambda invoke policy to the unauthenticated role

## Static webpage
1. Create a webpage
   - Bootstrap template used: https://getbootstrap.com/docs/4.4/getting-started/introduction/
   - Replace placeholder <## SOMETHING ##> tags with your values
2. Create an S3 bucket
3. Upload website content to the S3 bucket
4. Expose as a static website
   - AWS tutorial: https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html
