import csv
from telethon import TelegramClient, errors
from telethon.errors import FloodWaitError
from telethon.tl.functions.messages import SendMessageRequest

# Replace with your own API ID and Hash from my.telegram.org
API_ID = ''
API_HASH = ''

# Function to send messages to users
async def send_message(client, message, usernames):
    for username in usernames:
        try:
            print(f"Sending message to {username}")
            await client(SendMessageRequest(username, message))
            time.sleep(3)  # Delay of 3 seconds between messages to avoid Telegram limits
        except FloodWaitError as e:
            print(f"Flood wait error. Waiting {e.seconds} seconds")
            time.sleep(e.seconds)
        except Exception as e:
            print(f"Error sending message to {username}: {e}")

if __name__ == "__main__":
    # Create the Telegram client
    client = TelegramClient('session_name', API_ID, API_HASH)

    # Start the client and ask for login via phone number
    async def main():
        await client.start()
        
        # Ask the user for the message text file
        message_file = input("Enter the path to the message text file: ")
        with open(message_file, 'r') as f:
            message = f.read().strip()
        
        # Ask the user for the usernames file
        usernames_file = input("Enter the path to the usernames CSV file: ")
        with open(usernames_file, 'r') as f:
            usernames = [row[0] for row in csv.reader(f)]
        
        # Send the message to the list of usernames
        await send_message(client, message, usernames)

    # Run the client in async mode
    with client:
        client.loop.run_until_complete(main())
