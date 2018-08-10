#!/usr/bin/python3.6

import discord
import asyncio
import queue
from time import sleep
from tkn import *

client = discord.Client()

user_queue = queue.Queue(10)
voice_channel = None

@client.event
@asyncio.coroutine
def on_message(message):
    global voice_channel
    if (message.author.id == client.user.id):
        return

    if (message.content.startswith("!debate")):
        if (message.author.voice.voice_channel is None):
            yield from client.send_message(message.channel, "Fuck you, go in voice chat")
        else:
            voice_channel = message.author.voice.voice_channel
            yield from client.send_message(message.channel, message.author.mention + " wants to fight in " + voice_channel.name + " , go fuck him up nerds")

    if (message.content.startswith("!queue")):
        if (voice_channel is None):
            yield from client.send_message(message.channel, "There isn't a debate yet, start one with !debate while in a voice channel!")
        elif (message.author not in user_queue.queue and voice_channel == message.author.voice.voice_channel):
            yield from client.send_message(message.channel,
            message.author.mention + " joined the queue in " +
            str(len(user_queue.queue)) + "th position")
            user_queue.put(message.author)
        elif message.author in user_queue.queue:
            yield from client.send_message(message.channel, "You are already in queue!")
        else:
            yield from client.send_message(message.channel, "Fuck you, go to " + voice_channel.name)

    if (message.content.startswith("!skip")):
        yield from client.send_message(message.channel, user_queue.get_nowait().mention + " was skipped")

client.run(token)
