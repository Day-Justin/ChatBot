#Bot that follows you around and responds to you when you ask it a question

import discord
imoport os
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level = logging.INFO)
logging = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename = 'discord.log', encoding = 'utf-8', mode = 'w')
handler.setFormatter(logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(message)s')
logger.addHandler(handler)

intents = discord.Intents.all()

client = discord.Client(intents = intents)

@client.event 
ascync def on_ready():
	print(f'Hey! Listen')







TOKEN = os.getenv("NAVI_TOKEN")
clinet.run(TOKEN)

