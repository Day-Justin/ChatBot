#Bot that follows you around and responds to you when you ask it a question

import discord
import os
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename = 'discord.log', encoding = 'utf-8', mode = 'w')
handler.setFormatter(logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents.all()

client = discord.Client(intents = intents)

@client.event 
async def on_ready():
		print(f'Hey! Listen')
@client.event	
async def on_message(message):
		if message.author == client.user:
			return
		if message.content.startswith('$hello'):
			await message.channel.send('Hey! Listen') 






TOKEN = os.getenv("NAVI_TOKEN")
client.run(TOKEN)

