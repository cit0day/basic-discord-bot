import discord
from discord.ext import commands
import aiohttp

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Your Discord bot token
DISCORD_TOKEN = "YOUR_DISCORD_BOT_TOKEN"

# Your webhook URL
WEBHOOK_URL = "YOUR_DISCORD_WEBHOOK_URL"

# Role ID to assign when button is clicked
ROLE_ID = YOUR_ROLE_ID  # Replace with your role ID


class RoleButton(discord.ui.Button):
    def __init__(self):
        super().__init__(label="Get Role", style=discord.ButtonStyle.primary)

    async def callback(self, interaction: discord.Interaction):
        role = interaction.guild.get_role(ROLE_ID)
        if role:
            if role in interaction.user.roles:
                await interaction.user.remove_roles(role)
                await interaction.response.send_message(f"Role {role.name} removed!", ephemeral=True)
            else:
                await interaction.user.add_roles(role)
                await interaction.response.send_message(f"Role {role.name} added!", ephemeral=True)
        else:
            await interaction.response.send_message("Role not found!", ephemeral=True)


class RoleView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(RoleButton())


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@bot.command(name="send_webhook")
async def send_webhook(ctx, *, message: str):
    async with aiohttp.ClientSession() as session:
        webhook = discord.Webhook.from_url(WEBHOOK_URL, adapter=discord.AsyncWebhookAdapter(session))
        await webhook.send(message)
        await ctx.send("Message sent to webhook!")


@bot.command(name="create_button")
async def create_button(ctx):
    view = RoleView()
    await ctx.send("Click the button to get/remove the role:", view=view)


bot.run(DISCORD_TOKEN)
