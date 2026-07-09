import discord
from discord import app_commands
from dotenv import load_dotenv
import os
# import asyncio
# from logwatch import watch_logs

from minecraft import command

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
YOUR_CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

class MyBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)


bot = MyBot()


@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logged in as {bot.user}")


@bot.tree.command(name="mc")
@app_commands.describe(message="Message to send to Minecraft")
async def mc(interaction: discord.Interaction, message: str):

    # Send message into Minecraft chat
    command(f"say [Discord] {interaction.user.name}: {message}")

    await interaction.response.send_message(
        f"Sent message to Minecraft: {message}", ephemeral=True
    )


# @bot.event
# async def on_ready():

#     await bot.tree.sync()

#     print(f"Logged in as {bot.user}")

#     asyncio.create_task(
#         watch_logs(
#             bot,
#             YOUR_CHANNEL_ID
#         )
#     )


bot.run(TOKEN)