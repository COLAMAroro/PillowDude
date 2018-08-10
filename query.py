#!/usr/bin/python3.6

import discord
import asyncio
from time import sleep
from tkn import *

client = discord.Client()

queue = []

@client.event
@asyncio.coroutine
def on_message(message):
    if (message.author.id == client.user.id):
        return

    if (message.content.startswith("!queue")):
        yield from client.send_message(message.channel, message.author.mention + " joined the queue in " + str(len(queue)) + "th position")
        queue.append(message.author)

    if (message.content.startswith("!skip")):
        yield from client.send_message(message.channel, queue[0].mention + " was skipped")
        queue.pop(0)

client.run(token)
