#Bot that follows you around and responds to you when you ask it a question

import discord
imoport os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()

client = discord.Client(intents = intents)

@client.event 
ascync def on_ready():
	print(f'Hey! Listen')







TOKEN = os.getenv("NAVI_TOKEN")
clinet.run(TOKEN)

