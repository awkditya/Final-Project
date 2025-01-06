import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from twilio.rest import Client
import requests
from bs4 import BeautifulSoup
import pyttsx3
import pyautogui
import geocoder
import time

# Function to send an email
def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Failed to send email:", e)

# Function to send an SMS
def send_sms(account_sid, auth_token, from_number, to_number, message):
    try:
        client = Client(account_sid, auth_token)
        client.messages.create(body=message, from_=from_number, to=to_number)
        print("SMS sent successfully!")
    except Exception as e:
        print("Failed to send SMS:", e)

# Function to scrape top 5 Google search results
def scrape_google(query):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(f"https://www.google.com/search?q={query}", headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        results = []
        for g in soup.find_all('div', class_='BVG0Nb', limit=5):
            title = g.text
            link = g.find('a')['href']
            results.append((title, link))
        return results
    except Exception as e:
        print("Failed to scrape Google:", e)

# Function to get current geo-coordinates and location
def get_location():
    try:
        g = geocoder.ip('me')
        return g.latlng, g.address
    except Exception as e:
        print("Failed to get location:", e)

# Function to convert text to audio
def text_to_audio(text):
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("Failed to convert text to audio:", e)

# Function to control volume
def control_volume(action):
    try:
        if action == 'up':
            pyautogui.press('volumeup')
        elif action == 'down':
            pyautogui.press('volumedown')
        elif action == 'mute':
            pyautogui.press('volumemute')
        print("Volume action executed successfully!")
    except Exception as e:
        print("Failed to control volume:", e)

# Function to send bulk emails
def send_bulk_email(sender_email, sender_password, recipients, subject, body):
    for recipient in recipients:
        send_email(sender_email, sender_password, recipient, subject, body)

# Main menu for terminal application
def main():
    while True:
        print("\nChoose an option:")
        print("1. Send Email")
        print("2. Send SMS")
        print("3. Scrape Google")
        print("4. Get Location")
        print("5. Text-to-Audio")
        print("6. Control Volume")
        print("7. Send Bulk Email")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            sender_email = input("Enter your email: ")
            sender_password = input("Enter your password: ")
            recipient_email = input("Enter recipient email: ")
            subject = input("Enter subject: ")
            body = input("Enter message body: ")
            send_email(sender_email, sender_password, recipient_email, subject, body)

        elif choice == '2':
            account_sid = input("Enter Twilio SID: ")
            auth_token = input("Enter Twilio Auth Token: ")
            from_number = input("Enter Twilio phone number: ")
            to_number = input("Enter recipient phone number: ")
            message = input("Enter message: ")
            send_sms(account_sid, auth_token, from_number, to_number, message)

        elif choice == '3':
            query = input("Enter search query: ")
            results = scrape_google(query)
            for i, (title, link) in enumerate(results):
                print(f"{i + 1}. {title} ({link})")

        elif choice == '4':
            coords, address = get_location()
            print(f"Coordinates: {coords}, Address: {address}")

        elif choice == '5':
            text = input("Enter text to convert to audio: ")
            text_to_audio(text)

        elif choice == '6':
            action = input("Enter action (up, down, mute): ")
            control_volume(action)

        elif choice == '7':
            sender_email = input("Enter your email: ")
            sender_password = input("Enter your password: ")
            recipients = input("Enter recipient emails (comma-separated): ").split(',')
            subject = input("Enter subject: ")
            body = input("Enter message body: ")
            send_bulk_email(sender_email, sender_password, recipients, subject, body)

        elif choice == '8':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
