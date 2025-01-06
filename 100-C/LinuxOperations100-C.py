import os
import subprocess
import pywhatkit
import pyttsx3
from termcolor import colored
from art import text2art

def send_whatsapp_message():
    phone_number = input("Enter phone number (with country code): ")
    message = input("Enter message: ")
    pywhatkit.sendwhatmsg_instantly(phone_number, message)
    print("WhatsApp message sent!")

def speak_command_output():
    command = input("Enter a Linux command to execute: ")
    result = subprocess.getoutput(command)
    print(result)
    engine = pyttsx3.init()
    engine.say(result)
    engine.runAndWait()

def send_email():
    sender = input("Enter sender email: ")
    recipient = input("Enter recipient email: ")
    subject = input("Enter subject: ")
    body = input("Enter body: ")
    os.system(f'echo "{body}" | mail -s "{subject}" {recipient}')
    print("Email sent!")

def send_sms():
    phone_number = input("Enter phone number: ")
    message = input("Enter message: ")
    os.system(f'echo "{message}" | gammu sendsms TEXT {phone_number}')
    print("SMS sent!")

def setup_zoom_server():
    os.system("sudo apt update && sudo apt install zoom")
    print("Zoom server installed and ready!")

def post_to_social_media():
    platform = input("Enter platform (telegram/instagram/facebook/discord): ")
    message = input("Enter message: ")
    if platform.lower() == "telegram":
        os.system(f'echo "{message}" > telegram_post.txt')
    elif platform.lower() == "instagram":
        os.system(f'echo "{message}" > instagram_post.txt')
    elif platform.lower() == "facebook":
        os.system(f'echo "{message}" > facebook_post.txt')
    elif platform.lower() == "discord":
        os.system(f'echo "{message}" > discord_post.txt')
    print(f"Message posted to {platform}!")

def change_file_colors():
    print(colored("This file is red!", "red"))
    print(colored("This folder is blue!", "blue"))

def read_ram():
    with open("/proc/meminfo", "r") as f:
        print(f.read())

def change_gnome_terminal_theme():
    os.system("gsettings set org.gnome.desktop.interface gtk-theme 'Adwaita-dark'")
    print("GNOME terminal theme changed to dark!")

def create_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    os.system(f'sudo useradd {username}')
    os.system(f'echo "{username}:{password}" | sudo chpasswd')
    print(f"User {username} created with password!")

def run_linux_in_browser():
    os.system("firefox https://distrotest.net")
    print("Running Linux in browser!")

def google_search():
    query = input("Enter search query: ")
    os.system(f'xdg-open "https://www.google.com/search?q={query}"')

def run_windows_software():
    software = input("Enter Windows software to run (e.g., notepad): ")
    os.system(f'wine {software}')
    print(f"Running {software} on Linux!")

def sync_folders():
    folder1 = input("Enter source folder: ")
    folder2 = input("Enter destination folder: ")
    os.system(f'rsync -av {folder1} {folder2}')
    print("Folders synced!")

def print_ascii_art():
    text = input("Enter text to convert to ASCII art: ")
    print(text2art(text))

def main():
    while True:
        print("\nChoose an option:")
        print("1. Send WhatsApp Message")
        print("2. Speak Command Output")
        print("3. Send Email")
        print("4. Send SMS")
        print("5. Setup Zoom Server")
        print("6. Post to Social Media")
        print("7. Change File Colors")
        print("8. Read RAM")
        print("9. Change GNOME Terminal Theme")
        print("10. Create User")
        print("11. Run Linux in Browser")
        print("12. Google Search")
        print("13. Run Windows Software")
        print("14. Sync Folders")
        print("15. Print ASCII Art")
        print("16. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            send_whatsapp_message()
        elif choice == '2':
            speak_command_output()
        elif choice == '3':
            send_email()
        elif choice == '4':
            send_sms()
        elif choice == '5':
            setup_zoom_server()
        elif choice == '6':
            post_to_social_media()
        elif choice == '7':
            change_file_colors()
        elif choice == '8':
            read_ram()
        elif choice == '9':
            change_gnome_terminal_theme()
        elif choice == '10':
            create_user()
        elif choice == '11':
            run_linux_in_browser()
        elif choice == '12':
            google_search()
        elif choice == '13':
            run_windows_software()
        elif choice == '14':
            sync_folders()
        elif choice == '15':
            print_ascii_art()
        elif choice == '16':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
