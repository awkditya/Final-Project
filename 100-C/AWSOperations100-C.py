import boto3
import csv
import json
import os
import pymongo
from botocore.exceptions import NoCredentialsError

def launch_ec2_instance():
    ec2 = boto3.client('ec2')
    response = ec2.run_instances(
        ImageId='ami-0abcdef1234567890',  # Replace with RHEL AMI ID
        InstanceType='t2.micro',
        KeyName='MyKeyPair',  # Replace with your key pair
        SecurityGroupIds=['sg-12345678'],  # Replace with your security group
        SubnetId='subnet-12345678',  # Replace with your subnet ID
        MinCount=1,
        MaxCount=1,
        TagSpecifications=[{
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name', 'Value': 'RHEL-GUI-Instance'}]
        }]
    )
    print("EC2 Instance Launched:", response)

def access_logs_from_s3(bucket_name, local_dir):
    s3 = boto3.client('s3')
    try:
        s3.download_file(bucket_name, 'logs/', local_dir)
        print(f"Logs downloaded to {local_dir}")
    except NoCredentialsError:
        print("Credentials not available")

def transcribe_audio(event):
    transcribe = boto3.client('transcribe')
    s3 = boto3.client('s3')

    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']

    job_name = f"transcribe-{object_key.split('.')[0]}"
    file_uri = f"s3://{bucket_name}/{object_key}"
    output_bucket = "your-output-bucket-name"  # Replace with your bucket

    transcribe.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': file_uri},
        MediaFormat=object_key.split('.')[-1],
        LanguageCode='en-US',
        OutputBucketName=output_bucket
    )
    print("Transcription job started")

def connect_to_mongodb():
    mongo_uri = "mongodb://your-mongo-uri"
    client = pymongo.MongoClient(mongo_uri)
    db = client['your-database']
    collection = db['your-collection']
    data = {"name": "Test", "value": "Lambda to MongoDB"}
    collection.insert_one(data)
    print("Data inserted into MongoDB")

def upload_to_s3(file_name, bucket, object_name=None):
    s3 = boto3.client('s3')
    if object_name is None:
        object_name = file_name
    try:
        s3.upload_file(file_name, bucket, object_name)
        print(f"{file_name} uploaded to {bucket}/{object_name}")
    except NoCredentialsError:
        print("Credentials not available")

def lambda_s3_to_ses(event):
    s3 = boto3.client('s3')
    ses = boto3.client('ses')

    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']

    s3.download_file(bucket_name, object_key, '/tmp/emails.csv')

    with open('/tmp/emails.csv', 'r') as file:
        reader = csv.reader(file)
        emails = [row[0] for row in reader]

    for email in emails:
        ses.send_email(
            Source='your-email@example.com',
            Destination={'ToAddresses': [email]},
            Message={
                'Subject': {'Data': 'Hello from Lambda'},
                'Body': {'Text': {'Data': 'This is a test email'}}
            }
        )
    print("Emails sent successfully")

def main():
    while True:
        print("\nChoose an option:")
        print("1. Launch EC2 Instance")
        print("2. Access Logs from S3")
        print("3. Transcribe Audio File")
        print("4. Connect to MongoDB")
        print("5. Upload Object to S3")
        print("6. Process S3 to SES")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            launch_ec2_instance()
        elif choice == '2':
            bucket_name = input("Enter S3 bucket name: ")
            local_dir = input("Enter local directory to save logs: ")
            access_logs_from_s3(bucket_name, local_dir)
        elif choice == '3':
            # Simulated S3 event for testing
            event = {
                'Records': [
                    {
                        's3': {
                            'bucket': {'name': 'your-audio-bucket'},
                            'object': {'key': 'audio-file.mp3'}
                        }
                    }
                ]
            }
            transcribe_audio(event)
        elif choice == '4':
            connect_to_mongodb()
        elif choice == '5':
            file_name = input("Enter file name to upload: ")
            bucket = input("Enter S3 bucket name: ")
            upload_to_s3(file_name, bucket)
        elif choice == '6':
            # Simulated S3 event for testing
            event = {
                'Records': [
                    {
                        's3': {
                            'bucket': {'name': 'your-email-bucket'},
                            'object': {'key': 'emails.csv'}
                        }
                    }
                ]
            }
            lambda_s3_to_ses(event)
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
