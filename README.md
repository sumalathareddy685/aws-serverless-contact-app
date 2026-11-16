# AWS End-to-End Serverless Contact Application
A full-stack serverless web application built on AWS that captures user inquiries and stores them securely in a NoSQL database.

## Architecture & AWS Services Used
- **Amazon S3:** Hosts the static frontend (HTML5/JavaScript).
- **Amazon API Gateway (HTTP API):** Exposes a `/submit` REST endpoint with custom CORS policies.
- **AWS Lambda (Python 3.12 / Boto3):** Processes incoming JSON payloads and handles OPTIONS preflight requests.
- **Amazon DynamoDB:** Stores submitted contact details (`id`, `name`, `email`, `message`).
- **AWS IAM:** Follows least-privilege security using an execution role for Lambda-to-DynamoDB access.

## Key Challenges Solved
- **CORS Preflight Handling:** Configured `Access-Control-Allow-Origin` and `OPTIONS` route integration in API Gateway and Lambda to allow secure cross-origin requests from S3 static hosting.
