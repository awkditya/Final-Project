#!/bin/bash

# 1. Send WhatsApp Message using terminal
# You need to use WhatsApp API or a tool like `yowsup` or `whatsapp-cli`.
# Example using `whatsapp-cli`:
whatsapp-cli send --phone "recipient_phone_number" --message "Hello from terminal!"

# 2. Output of a command should be spoken from the speaker
# Install `espeak` for text-to-speech functionality
espeak "Hello, this is a test message"

# 3. Send Email from Linux Terminal
# You can use `sendmail` or `mail` command for this.
echo "Subject: Test Email" | sendmail recipient@example.com

# 4. Send SMS using terminal
# Using Twilio API to send SMS
curl -X POST https://api.twilio.com/2010-04-01/Accounts/your_account_sid/Messages.json \
--data-urlencode "Body=Hello, this is a test message" \
--data-urlencode "From=+1234567890" \
--data-urlencode "To=+1987654321" \
-u your_account_sid:your_auth_token

# 5. Use Linux as a Zoom server
# Install `zoom` from Zoom's official website or using package manager (e.g., apt, yum).
# Example:
sudo apt install zoom

# Start Zoom (GUI):
zoom &

# 6. Make a post in Telegram, Instagram, Facebook, Discord from the Linux terminal
# Telegram:
curl -X POST https://api.telegram.org/bot<your_bot_token>/sendMessage -d chat_id=<chat_id> -d text="Hello from terminal!"
# Instagram and Facebook: Use their official APIs (requires authentication tokens).
# Discord:
curl -X POST -H "Authorization: Bot <your_bot_token>" -d '{"content": "Hello from terminal!"}' https://discord.com/api/v9/channels/<channel_id>/messages

# 7. Change the color of files and folders in Linux
# You can use `LS_COLORS` environment variable to change the colors of files.
# Example: Change the color of directories to green.
export LS_COLORS="di=0;32"  # Green color for directories

# 8. Reading the entire RAM
# You can use `free` or `vmstat` to check memory usage.
free -h

# 9. Change the look and feel of GNOME terminal
# You can change GNOME Terminal settings via `dconf` or GUI.
# Example: Change the background color using `dconf`:
dconf write /org/gnome/terminal/legacy/profiles:/background-color "'#000000'"

# 10. Create user and set password
# Use `useradd` and `passwd` commands.
sudo useradd newuser
sudo passwd newuser

# 11. Running Linux in the browser
# You can use tools like `shellinabox` or `guacamole` to run Linux in the browser.
# Install `shellinabox`:
sudo apt install shellinabox
# Start it:
sudo service shellinabox start

# 12. Google search from terminal
# Use `googler` or `lynx` to search Google from the terminal.
# Example with `googler`:
googler "Linux tutorial"

# 13. Run Windows software (e.g., Notepad) in Linux
# Use Wine to run Windows applications on Linux.
sudo apt install wine
wine notepad.exe

# 14. Sync two different folders in Linux (interactive)
# Use `rsync` to sync folders. It will prompt the user for folder paths.
echo "Enter source folder path:"
read source
echo "Enter destination folder path:"
read destination
rsync -avh --progress $source $destination

# 15. Convert command output to ASCII art
# Install `figlet` for ASCII art.
sudo apt install figlet
echo "Hello from terminal" | figlet
