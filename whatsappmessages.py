import pywhatkit as kit
import pyautogui
import time

# List of phone numbers (with country code)
phone_numbers = ["+923172417634","+923232991914","+923270579436","+923193949557","+923325886374","+923335867489","+923260054089"]

# Message to send
message = "Aoa i am a developer how can i help you for more details visit my website wswebsolutions.000webhostapp.com         My skills php,dotnet, flutter,wordpress, digital marketing            I am a contract based freelancer "

# Delay between actions
delay = 10

# Function to send messages
def send_messages():
    for number in phone_numbers:
        # Get the current time
        current_hour = time.localtime().tm_hour
        current_minute = time.localtime().tm_min

        # Calculate the minute to send the message
        send_minute = current_minute + 2
        send_hour = current_hour

        if send_minute >= 60:
            send_minute -= 60
            send_hour += 1

        if send_hour >= 24:
            send_hour -= 24

        # Schedule the message
        kit.sendwhatmsg(number, message, send_hour, send_minute)

        # Wait for WhatsApp Web to open and the message to be typed
        time.sleep(delay)

        # Press the Enter key to send the message
        pyautogui.press("enter")

        # Wait for a short time before sending the next message
        time.sleep(5)

# Send the messages
send_messages()

print("Messages sent successfully.")
