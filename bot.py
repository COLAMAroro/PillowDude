import discord
import asyncio
from tkn import *

client = discord.Client()

@client.event
@asyncio.coroutine
def on_ready():
	print("Bot is ready")
	print(client.user.name)
	print(client.user.id)

@client.event
@asyncio.coroutine
def on_message(message):
	if message.channel.is_private and message.author.id != client.user.id:
		client.send_message(message.channel, "Sorry, I can't do anything in private")
		return
	ping = "<@" + client.user.id + ">"
	if message.content.startswith(ping):
		yield from token_gestion(message, message.content[len(ping):])

@asyncio.coroutine
def token_gestion(message, command):
	print("Received a message")

client.run(token)