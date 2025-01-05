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
import subprocess
import figlet

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
        server.starttls()
        server.login(from_email, password)
        
        for to_email in to_emails:
            msg['To'] = to_email
            text = msg.as_string()
            server.sendmail(from_email, to_email, text)
        
        server.quit()
        print('Bulk emails sent successfully')
    except Exception as e:
        print(f'Error: {e}')

# 9. Send WhatsApp Message Using Twilio API
def send_whatsapp_message(to_number, message):
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message,
        from_='whatsapp:+14155238886',  # Twilio sandbox number
        to=f'whatsapp:{to_number}'
    )

    print(f'WhatsApp message sent to {to_number}')

# 10. Output Command Result as Audio
def output_as_audio(command):
    result = os.popen(command).read()
    text_to_audio(result)

# 11. Change the Color of Files and Folders in Linux
def change_file_colors():
    os.system('export LS_COLORS="di=1;34:fi=0;32"')

# 12. Reading the Entire RAM
def read_ram():
    os.system('cat /proc/meminfo')

# 13. Change the Look and Feel of GNOME Terminal
def change_gnome_terminal():
    os.system('gnome-terminal --preferences')

# 14. Create User and Set Password
def create_user(username, password):
    os.system(f'sudo adduser {username}')
    os.system(f'echo "{username}:{password}" | sudo chpasswd')

# 15. Run Linux in the Browser (Using Webminal or Web-based Terminal)
def run_linux_in_browser():
    print("Use Webminal or GoLinuxCloud to run Linux in the browser.")

# 16. Google Search from Terminal (Using Googler)
def google_search_terminal(query):
    os.system(f'googler {query}')

# 17. Run Windows Software (e.g., Notepad) in Linux
def run_windows_software():
    os.system('wine notepad.exe')

# 18. Sync Two Different Folders in Linux
def sync_folders():
    source = input("Enter source folder path: ")
    destination = input("Enter destination folder path: ")
    os.system(f'rsync -avh {source} {destination}')

# 19. Convert Text to ASCII Art
def text_to_ascii_art(text):
    os.system(f'figlet "{text}"')

# Example Usage:
send_email('Test Subject', 'This is the email body', 'recipient@example.com')
send_sms('+1987654321', 'Hello, this is a test message.')
results = google_search('Python programming')
for i, result in enumerate(results, 1):
    print(f'{i}. {result}')
get_location()
text_to_audio('Hello, I am your assistant!')
set_volume(50)
send_sms_from_mobile('1234567890', 'Hello from Python!')
to_emails = ['recipient1@example.com', 'recipient2@example.com']
send_bulk_email('Bulk Email Subject', 'This is the email body', to_emails)
send_whatsapp_message('+1234567890', 'Hello via WhatsApp!')
output_as_audio('ls -l')
change_file_colors()
read_ram()
change_gnome_terminal()
create_user('newuser', 'password123')
run_linux_in_browser()
google_search_terminal('Python tutorials')
run_windows_software()
sync_folders()
text_to_ascii_art('Hello, Linux!')
