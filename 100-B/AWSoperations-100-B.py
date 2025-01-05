#!/bin/bash

# 1. Launch EC2 Instance (Amazon Linux 2 or RHEL)
# Launch an EC2 instance with a specific AMI, instance type, and key pair.
aws ec2 run-instances --image-id ami-xxxxxxxxxxxxxxx --count 1 --instance-type t2.micro --key-name your-key-pair --security-group-ids sg-xxxxxxxx --subnet-id subnet-xxxxxxxx --associate-public-ip-address

# 2. Launch RHEL GUI Instance in Cloud
# Use AWS EC2 to launch a Red Hat Enterprise Linux instance with GUI.
aws ec2 run-instances --image-id ami-xxxxxxxxxxxxxxx --count 1 --instance-type t2.medium --key-name your-key-pair --security-group-ids sg-xxxxxxxx --subnet-id subnet-xxxxxxxx --associate-public-ip-address --user-data file://rhel-gui-setup.sh

# 3. Access Logs from Cloud
# Use CloudWatch Logs to view logs from your EC2 instances.
aws logs describe-log-groups
aws logs get-log-events --log-group-name /aws/lambda/your-lambda-function-name --log-stream-name log-stream-name

# 4. Event-Driven Architecture (Audio File to Text using AWS Transcribe)
# Create an S3 event that triggers AWS Lambda when an audio file is uploaded to S3.

# Create a Lambda function to process audio files.
aws lambda create-function --function-name transcribe-audio --runtime python3.8 --role arn:aws:iam::your-account-id:role/your-lambda-role --handler transcribe_audio.handler --zip-file fileb://transcribe_audio.zip

# Create an S3 bucket event notification to trigger the Lambda function.
aws s3api put-bucket-notification-configuration --bucket your-bucket-name --notification-configuration file://s3-notification-config.json

# `s3-notification-config.json` should contain the following:
# {
#   "LambdaFunctionConfigurations": [
#     {
#       "LambdaFunctionArn": "arn:aws:lambda:region:account-id:function:transcribe-audio",
#       "Events": ["s3:ObjectCreated:*"],
#       "Filter": {
#         "S3Key": {
#           "FilterRules": [
#             {
#               "Name": "suffix",
#               "Value": ".mp3"
#             }
#           ]
#         }
#       }
#     }
#   ]
# }

# 5. Connect Python to MongoDB Service of AWS using Lambda
# Lambda function to connect to MongoDB and store data.

import pymongo
import json

def lambda_handler(event, context):
    client = pymongo.MongoClient("mongodb://your-mongodb-uri")
    db = client['your-database']
    collection = db['your-collection']
    data = json.loads(event['body'])
    collection.insert_one(data)
    return {
        'statusCode': 200,
        'body': json.dumps('Data inserted successfully')
    }

# 6. Uploading Any Object to S3
aws s3 cp your_file.txt s3://your-bucket-name/your_file.txt

# 7. Integrate Lambda with S3 to Send Emails Using SES
# Create a Lambda function that reads email IDs from a file in S3 and sends an email via SES.

import boto3
import json

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    ses = boto3.client('ses')
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']
    
    # Retrieve the file from S3
    s3_object = s3.get_object(Bucket=bucket_name, Key=file_name)
    email_ids = s3_object['Body'].read().decode('utf-8').splitlines()
    
    # Send emails using SES
    for email in email_ids:
        response = ses.send_email(
            Source='your-email@example.com',
            Destination={
                'ToAddresses': [email]
            },
            Message={
                'Subject': {
                    'Data': 'Test Email'
                },
                'Body': {
                    'Text': {
                        'Data': 'This is a test email from AWS Lambda!'
                    }
                }
            }
        )
        print(f"Email sent to {email}: {response}")

# Upload the Lambda function and set the necessary permissions for SES and S3.

import boto3
import json

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    transcribe = boto3.client('transcribe')
    
    # Get the S3 bucket and file name from the event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']
    
    # Start transcription job
    job_name = file_name.split('.')[0]
    job_uri = f"s3://{bucket_name}/{file_name}"
    
    transcribe.start_transcription_job(
        TranscriptionJobName=job_name,
        LanguageCode='en-US',
        Media={'MediaFileUri': job_uri},
        MediaFormat='mp3',
        OutputBucketName='your-output-bucket'
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps(f"Transcription job started for {file_name}")
    }

import pymongo
import json

def lambda_handler(event, context):
    client = pymongo.MongoClient("mongodb://your-mongodb-uri")
    db = client['your-database']
    collection = db['your-collection']
    data = json.loads(event['body'])
    collection.insert_one(data)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Data inserted successfully')
    }

import boto3
import json

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    ses = boto3.client('ses')
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']
    
    # Retrieve the file from S3
    s3_object = s3.get_object(Bucket=bucket_name, Key=file_name)
    email_ids = s3_object['Body'].read().decode('utf-8').splitlines()
    
    # Send emails using SES
    for email in email_ids:
        response = ses.send_email(
            Source='your-email@example.com',
            Destination={
                'ToAddresses': [email]
            },
            Message={
                'Subject': {
                    'Data': 'Test Email'
                },
                'Body': {
                    'Text': {
                        'Data': 'This is a test email from AWS Lambda!'
                    }
                }
            }
        )
        print(f"Email sent to {email}: {response}")
