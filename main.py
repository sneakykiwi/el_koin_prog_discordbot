import discord, os
from discord.ext import commands
from colorama import init
from termcolor import colored


from Cogs import Autorole


client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    init()
    print(colored(f'Welcome to {client.user.name} discord bot!\n', 'yellow'))
    print(colored(f'Status: Logged in', 'green'))
    print(colored(f'Username: {client.user.name}', 'green'))
    print(colored(f'Client ID: {client.user.id}', 'green'))
    print(colored(
        f'Invite URL: {discord.utils.oauth_url(client.user.id)}&permissions=8\n', 'green'))
    await client.change_presence(activity=discord.Activity(name=f"Made by Kiwi!", type=discord.ActivityType.listening))

Autorole.setup(client=client, member_role_id=725681956804886529, welcome_channel_id=725474351440199684)

client.run(os.getenv('CLIENT_TOKEN'))
