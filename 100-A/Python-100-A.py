# Install necessary libraries
pip install smtplib twilio googlesearch-python geopy pyttsx3 pycaw

# Create a Python script with the following content
echo "
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from twilio.rest import Client
from googlesearch import search
from geopy.geocoders import Nominatim
import requests
import pyttsx3
from pycaw.pycaw import AudioUtilities
from ctypes import cast, POINTER
import os

# 1. Send Email Message Using Python Code
def send_email(subject, body, to_email):
    from_email = 'your_email@example.com'
    password = 'your_password'
    
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
        print('Email sent successfully')
    except Exception as e:
        print(f'Error: {e}')

# 2. Send SMS Message Using Python Code
def send_sms(to_number, message):
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
        body=message,
        from_='+1234567890',  # Your Twilio number
        to=to_number
    )
    
    print(f'Message sent to {to_number}')

# 3. Scrape Top 5 Search Results from Google Using Python Code
def google_search(query):
    results = []
    for result in search(query, num_results=5):
        results.append(result)
    return results

# 4. Find Current Geo Coordinates and Location Using Python Code
def get_location():
    response = requests.get('http://ipinfo.io')
    data = response.json()
    location = data['loc'].split(',')
    latitude = location[0]
    longitude = location[1]
    
    geolocator = Nominatim(user_agent='geoapiExercises')
    location = geolocator.reverse((latitude, longitude))
    
    print(f'Latitude: {latitude}, Longitude: {longitude}')
    print(f'Location: {location.address}')

# 5. Convert Text-to-Audio Using Python Code
def text_to_audio(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# 6. Control Volume of Your Laptop Using Python
def set_volume(level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        AudioUtilities.IID_IAudioEndpointVolume, 1, None)
    volume = cast(interface, POINTER(AudioUtilities.IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(level / 100, None)
    print(f'Volume set to {level}%')

# 7. Connect to Your Mobile and Send SMS from Your Mobile Messaging App Using Python
def send_sms_from_mobile(phone_number, message):
    os.system(f'adb shell am start -a android.intent.action.SENDTO -d sms:{phone_number} --es sms_body \"{message}\" --ez exit_on_sent true')

# 8. Create a Function to Send Bulk Email Using Python
def send_bulk_email(subject, body, to_emails):
    from_email = 'your_email@example.com'
    password = 'your_password'
    
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
     
