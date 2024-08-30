import discord
from discord.ext import commands
import os

# Intents are required for accessing more features of the Discord API
intents = discord.Intents.default()
intents.message_content = True  # Enable access to message content

# Create the bot instance
bot = commands.Bot(command_prefix="!", intents=intents)

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Simple test command
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Run the bot
bot.run(os.environ['YOUR_BOT_TOKEN'])

