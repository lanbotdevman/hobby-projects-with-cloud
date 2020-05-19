# web-comments-aws-lambda-dynamodb-s3

A simple static webpage with ability to save comments into AWS cloud:
- **DynamoDB to store the web comments**
   - Keep all the comments in a single partition
   - Content is sorted based on received timestamp
- **Lambda function to sanitize the content**
   - Adds server-side metadata
   - Avoids CSS attacks
- **Static webpage**
   - Using Bootstrap/jQuery template
   - Exposed via S3: Simple Storage Service

Given instructions are not intended as a complete end-to-end walkthrough, but rather serve the purpose of highlighting key steps for training or presentation activity.

## DynamoDB to store the web comments

1. Create a DynamoDB table
   - Key ‘id’ is a string (constant value from Lambda)
   - Sort key ‘timestamp’ is an integer (generated from Lambda)
2. Add a mock entry
   - Constant ID: ‘webcomments’
   - Timestamp (in seconds): 1583928000
   - Comment text as ‘commentText’ parameter

## Lambda function to sanitize data

1. Create a Lambda function
   - Author from scratch
   - Latest Python runtime
2. Import example Python code from GitHub:
   - [web-comments-aws-lambda-dynamodb-s3/lambda_public_api_endpoint/lambda_function.py](https://github.com/lanbotdevman/hobby-projects-with-cloud/blob/master/web-comments-aws-lambda-dynamodb-s3/lambda_public_api_endpoint/lambda_function.py)
3. Configure the table name to be used
   - Add ‘WEB_COMMENTS_TABLE_NAME’ environment property
4. Add test cases

### Handling permissions

AWS IAM (Identity and Access Management):
- Role: cross-service operations are done in a certain role
- Policy: permission to do something (attached to roles)

Granting access for the DynamoDB table and Lambda function:
1. Create an IAM policy for DynamoDB access
   - Permissions: Query and PutItem
   - Attach to the auto-generated Lambda execution role
2. Create an IAM policy for invoking Lambda
   - Permission: InvokeFunction
3. Create public Identity Pool in Cognito
   - Enable access to unauthenticated identities
   - Attach Lambda invoke policy to the unauthenticated role

## Static webpage
1. Create a webpage
   - Import example HTML code from GitHub: [web-comments-aws-lambda-dynamodb-s3/s3_static_web_files/index_template.html](https://github.com/lanbotdevman/hobby-projects-with-cloud/blob/master/web-comments-aws-lambda-dynamodb-s3/s3_static_web_files/index_template.html)
   - Replace placeholder <## KEY ##> tags with your values
2. Create an S3 bucket
3. Expose as a static website
   - Make it public and add a wildcard access policy: [](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html)
4. Upload website content to the S3 bucket

## Solution overview

![Solution overview diagram](https://www.plantuml.com/plantuml/proxy?src=https://raw.githubusercontent.com/lanbotdevman/hobby-projects-with-cloud/master/web-comments-aws-lambda-dynamodb-s3/solution_overview.puml)
