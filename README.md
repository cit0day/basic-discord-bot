# Discord Bot

## Setup Instructions

```bash
Create a Discord bot:
Go to the Discord Developer Portal.
Create a new application and then create a bot user.
Add the bot to your server with the appropriate permissions.
Get your Webhook URL:
Go to your Discord server.
Create a new webhook in one of the channels and copy the URL.
```

### Install dependencies:

```bash
pip install discord.py
pip install aiohttp```

### Usage
```bash
Usage
Send a message to a webhook:
In your Discord server, use the command !send_webhook Your message here.

The bot will send "Your message here" to the specified webhook.

Create a button for role assignment:
In your Discord server, use the command !create_button.

The bot will create a button that users can click to get or remove a role.

Notes
Replace YOUR_DISCORD_BOT_TOKEN with your bot's token.
Replace YOUR_DISCORD_WEBHOOK_URL with your webhook URL.
Replace YOUR_ROLE_ID with the ID of the role you want to assign.
This bot provides basic functionality to send messages to a webhook and assign/remove roles using buttons. You can expand its functionality as needed.
```
