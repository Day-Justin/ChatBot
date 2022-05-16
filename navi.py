#Bot that follows you around and responds to you when you ask it a question

import discord
import os
import random
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

		#logs the messages and channels
		userName = str(message.author).split('#')[0]
		userMessage = str(message.content)
		channel = str(message.channel.name)
		
		if message.author == client.user:
			return

		if message.channel.name == 'bot':
			if userMessage.lower() == 'hello':
				await message.channel.send(f'Hey {userName}! Listen')
				return
			
			if userMessage.lower() == 'bye':
				await message.channel.send(f'Hey {userName}! Bye')
				return

			if userMessage.lower() == 'random':
				response = f'Hey! Listen: {random.randrange(10000000)}'
				await message.channel.send(response)
				return 

		if userMessage.lower() == 'anywhere':
			await message.channel.send('Thought you could run from Hey! Listen huh')
			return
			
TOKEN = os.getenv("NAVI_TOKEN")
client.run(TOKEN)

