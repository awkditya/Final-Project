# 1. Send Email Message Using Python
import smtplib

def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(sender_email, recipient_email, message)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
# send_email("your_email@gmail.com", "your_password", "recipient_email@gmail.com", "Test Subject", "Test Body")

# 2. Send SMS Message Using Python
from twilio.rest import Client

def send_sms(account_sid, auth_token, from_phone, to_phone, message):
    client = Client(account_sid, auth_token)
    message = client.messages.create(body=message, from_=from_phone, to=to_phone)
    print(f"Message sent: {message.sid}")

# Example usage
# send_sms("your_account_sid", "your_auth_token", "+1234567890", "+0987654321", "Hello from Python!")

# 3. Scrape Top 5 Search Results from Google
import requests
from bs4 import BeautifulSoup

def scrape_google(query):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(f"https://www.google.com/search?q={query}", headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.select('.tF2Cxc')[:5]  # Select top 5 results
    for i, result in enumerate(results, 1):
        title = result.select_one('.DKV0Md').text
        link = result.select_one('.yuRUbf a')['href']
        print(f"{i}. {title} - {link}")

# Example usage
# scrape_google("Python programming")

# 4. Find Current Geo Coordinates and Location
import geocoder

def get_location():
    g = geocoder.ip('me')
    print(f"Latitude: {g.lat}, Longitude: {g.lng}, Address: {g.address}")

# Example usage
# get_location()

# 5. Convert Text to Audio
from gtts import gTTS
import os

def text_to_audio(text, filename="output.mp3"):
    tts = gTTS(text)
    tts.save(filename)
    os.system(f"start {filename}")

# Example usage
# text_to_audio("Hello, this is a text-to-speech conversion.")

# 6. Control Laptop Volume
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL

def set_volume(level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)
    volume.SetMasterVolumeLevelScalar(level / 100, None)

# Example usage (set volume to 50%)
# set_volume(50)

# 7. Connect to Mobile and Send SMS Using Mobile Messaging App
import os

def send_sms_via_adb(phone_number, message):
    os.system(f'adb shell service call isms 7 i32 1 s16 "com.android.mms.service" s16 "{phone_number}" s16 "null" s16 "{message}"')

# Example usage
# send_sms_via_adb("1234567890", "Hello from Python via ADB!")

# 8. Send Bulk Emails

def send_bulk_emails(sender_email, sender_password, recipient_emails, subject, body):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        for recipient_email in recipient_emails:
            message = f"Subject: {subject}\n\n{body}"
            server.sendmail(sender_email, recipient_email, message)
        server.quit()
        print("Bulk emails sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
# send_bulk_emails(
#     "your_email@gmail.com", "your_password",
#     ["email1@gmail.com", "email2@gmail.com"],
#     "Test Subject", "Test Body"
# )
