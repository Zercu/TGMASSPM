
```markdown
# Telegram Mass Messaging Script

This Python script allows you to send direct messages (PM) to multiple users through your **Telegram user account** using the [Telethon](https://docs.telethon.dev/en/latest/) library. The script logs into your Telegram account using your API credentials and sends messages to a list of users with a configurable delay between each message to avoid rate-limiting.

## Features
- **Automated PM**: Automatically sends messages to a list of users provided in a CSV file.
- **3-second interval**: Includes a delay between messages to comply with Telegram rate-limits.
- **Error handling**: Manages Telegram's rate limits with `FloodWaitError`, preventing account suspension from spamming.

## Requirements
- **Python 3.x**
- [Telethon](https://docs.telethon.dev/) library

## Setup

### 1. Get API ID and API Hash
You will need your **API ID** and **API Hash** from Telegram to authenticate your account:
1. Go to [my.telegram.org](https://my.telegram.org/).
2. Log in using your phone number.
3. Navigate to the API development tools section.
4. Copy your **API ID** and **API Hash**.

### 2. Install Python and Required Packages

Make sure you have Python 3 installed. Then, install the `Telethon` package by running the following command:

```bash
pip3 install telethon
```

### 3. Clone the Repository

Clone this repository to your local system:

```bash
git clone https://github.com/<your_username>/<repo_name>.git
cd <repo_name>
```

### 4. Update the Script

Replace the placeholders in the script with your **API ID** and **API Hash**:

```python
API_ID = 'YOUR_API_ID'
API_HASH = 'YOUR_API_HASH'
```

### 5. Create Input Files

- **Message file**: Create a text file (`message.txt`) containing the message you want to send.
- **Usernames file**: Create a CSV file (`usernames.csv`) with a list of usernames (one username per line). Example:

```
username1
username2
username3
```

## Usage

1. **Run the script**:
   Execute the script using Python:

   ```bash
   python3 telegram_mass_message.py
   ```

2. **Follow the prompts**:
   The script will ask for:
   - The path to the message text file.
   - The path to the usernames CSV file.

3. **Login**:
   When running the script for the first time, it will ask for your phone number and Telegram will send you a login code. Input the code to authenticate your session.

4. **Sending messages**:
   After logging in, the script will automatically send your message to each user listed in the CSV file with a 3-second delay between each message.

### Example Workflow

1. The script asks for the message file path:
   ```
   Enter the path to the message text file: message.txt
   ```

2. The script asks for the usernames file path:
   ```
   Enter the path to the usernames CSV file: usernames.csv
   ```

3. The script sends messages and displays success messages for each user:
   ```
   Sending message to username1
   Sending message to username2
   Sending message to username3
   ```

## Important Notes

- **Rate Limiting**: Telegram has strict limits on how many messages you can send within a short period. The script includes a 3-second delay to reduce the chances of getting temporarily restricted.
- **FloodWait Handling**: If Telegram enforces a wait time due to rate-limiting, the script will pause for the required time before continuing.
- **CSV Format**: The list of usernames should be provided in a CSV file with **one username per line**.

## Contributing

Feel free to open issues or submit pull requests if you'd like to improve this script.

## License

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


### Explanation of Key Sections:
- **Features**: A summary of what the script can do.
- **Setup**: A step-by-step guide on how to set up the project, including obtaining API credentials and installing dependencies.
- **Usage**: Instructions on how to run the script and what files you need to prepare.
- **Important Notes**: Reminders and considerations to help the user avoid account suspension from spamming.
