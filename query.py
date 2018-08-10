#!/usr/bin/python3.6

import discord
import asyncio
import queue
from time import sleep
from tkn import *

client = discord.Client()

user_queue = queue.Queue(10)

@client.event
@asyncio.coroutine
def on_message(message):
    if (message.author.id == client.user.id):
        return

    if (message.content.startswith("!queue")):
        if (message.author not in user_queue.queue):
            yield from client.send_message(message.channel, message.author.mention + " joined the queue in " + str(len(user_queue.queue)) + "th position")
            user_queue.put(message.author)
        else:
            yield from client.send_message(message.channel, "You are already in queue!")

    if (message.content.startswith("!skip")):
        yield from client.send_message(message.channel, user_queue.get_nowait().mention + " was skipped")

client.run(token)
