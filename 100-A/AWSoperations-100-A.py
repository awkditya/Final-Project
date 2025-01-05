import boto3
import os
import time
import json
import pymongo
import requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from twilio.rest import Client
from googlesearch import search
from geopy.geocoders import Nominatim
import pyttsx3
from pycaw.pycaw import AudioUtilities
from ctypes import cast, POINTER


# 1. Launch EC2 Instance (RHEL GUI)
def launch_ec2():
    ec2 = boto3.client('ec2')
    response = ec2.run_instances(
        ImageId='ami-xxxxxxxx',  # Replace with RHEL AMI ID
        InstanceType='t2.micro',
        MinCount=1,
        MaxCount=1,
        SecurityGroupIds=['sg-xxxxxxxx'],  # Replace with your security group
        KeyName='your-key-pair'  # Replace with your key pair
    )
    print(f"EC2 Instance launched: {response['Instances'][0]['InstanceId']}")


# 2. Access Logs from EC2 (CloudWatch)
def enable_cloudwatch_logs():
    ec2 = boto3.client('ec2')
    ec2.create_tags(
        Resources=['i-xxxxxxxx'],  # Replace with your EC2 instance ID
        Tags=[{'Key': 'Name', 'Value': 'EC2-Logs'}]
    )
    print("CloudWatch Logs enabled for EC2 instance.")


# 3. Event-Driven Architecture (Audio to Text Conversion)
def transcribe_audio(event, context):
    s3 = boto3.client('s3')
    transcribe = boto3.client('transcribe')

    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']
    job_name = f"transcription-{int(time.time())}"
    job_uri = f"s3://{bucket_name}/{file_key}"

    response = transcribe.start_transcription_job(
        TranscriptionJobName=job_name,
        LanguageCode='en-US',
        Media={'MediaFileUri': job_uri},
        MediaFormat='mp3',
        OutputBucketName=bucket_name
    )
    print(f"Transcription started for {file_key}")


# 4. MongoDB Connection in Lambda
def connect_to_mongo():
    client = pymongo.MongoClient(os.environ['MONGO_URI'])
    db = client['your_database']
    collection = db['your_collection']
    collection.insert_one({'name': 'AWS Lambda', 'task': 'MongoDB Connection'})
    print("MongoDB connection successful.")


# 5. Upload Object to S3
def upload_to_s3(file_name, bucket_name):
    s3 = boto3.client('s3')
    s3.upload_file(file_name, bucket_name, file_name)
    print(f"File {file_name} uploaded to {bucket_name}")


# 6. Lambda Function to Send Emails Using SES
def send_bulk_email(event, context):
    s3 = boto3.client('s3')
    ses = boto3.client('ses')

    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']
    obj = s3.get_object(Bucket=bucket_name, Key=file_key)
    email_ids = obj['Body'].read().decode('utf-8').splitlines()

    for email in email_ids:
        response = ses.send_email(
            Source='your_email@example.com',
            Destination={'ToAddresses': [email]},
            Message={
                'Subject': {'Data': 'Subject of the email'},
                'Body': {'Text': {'Data': 'Body of the email'}}
            }
        )
        print(f"Email sent to {email}")


# 7. Send Email Using Python
def send_email(subject, body, to_email):
    from_email = "your_email@example.com"
    password = "your_password"
    
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Error: {e}")


# 8. Send SMS Using Python (Twilio)
def send_sms(to_number, message):
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
        body=message,
        from_='+1234567890',  # Your Twilio number
        to=to_number
    )
    
    print(f"Message sent to {to_number}")


# 9. Scrape Top 5 Google Search Results
def google_search(query):
    results = []
    for result in search(query, num_results=5):
        results.append(result)
    return results


# 10. Find Current Geo Coordinates and Location
def get_location():
    response = requests.get("http://ipinfo.io")
    data = response.json()
    location = data['loc'].split(',')
    latitude = location[0]
    longitude = location[1]
    
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse((latitude, longitude))
    
    print(f"Latitude: {latitude}, Longitude: {longitude}")
    print(f"Location: {location.address}")


# 11. Convert Text to Audio
def text_to_audio(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


# 12. Control Volume of Laptop
def set_volume(level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        AudioUtilities.IID_IAudioEndpointVolume, 1, None)
    volume = cast(interface, POINTER(AudioUtilities.IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(level / 100, None)
    print(f"Volume set to {level}%")


# 13. Connect to Mobile and Send SMS
def send_sms_from_mobile(phone_number, message):
    os.system(f"adb shell am start -a android.intent.action.SENDTO -d sms:{phone_number} --es sms_body '{message}' --ez exit_on_sent true")


# Example Usage
if __name__ == "__main__":
    send_email("Test Subject", "This is the email body", "recipient@example.com")
    send_sms('+1987654321', 'Hello, this is a test message.')
    results = google_search("Python programming")
    for i, result in enumerate(results, 1):
        print(f"{i}. {result}")
    get_location()
    text_to_audio("Hello, I am your assistant!")
    set_volume(50)  # Set volume to 50%
    send_sms_from_mobile('1234567890', 'Hello from Python!')
