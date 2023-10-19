import discord
import os
import requests


nasa = os.getenv("NASA")
discord_token = os.getenv("DISCORD")

url = f"https://api.nasa.gov/planetary/apod?api_key={nasa}"

response = requests.request("GET", url).json()
space = response['hdurl']


intents = discord.Intents.default()
intents.message_content = True


client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('apod'):
        await message.channel.send(space)


client.run(f'{discord_token}')
