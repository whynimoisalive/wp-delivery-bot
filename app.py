import pywhatkit
import random
import time

def send_whatsapp_message(contact_name: str, message: str):
    try:
        # Send message instantly to the contact
        pywhatkit.sendwhatmsg_to_group_instantly(
            group_id=contact_name,
            message=message,
            wait_time=25  # Waits 10 seconds before sending the message
        )
        print(f"Message sent successfully to {contact_name}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    messages = [
        "Hello! How are you?",
        "Just checking in. Hope you're having a great day!",
        "Random message alert! 🚨",
        "Thought I'd say hi. Hi!",
        "Hope this message finds you well."
    ]
    
    contact_name = "Meta AI"  # The name of the contact as it appears in WhatsApp
    random_message = random.choice(messages)

    send_whatsapp_message(contact_name, random_message)

    # Wait for a few seconds to allow the message to be sent
    time.sleep(15)

if __name__ == "__main__":
    main()