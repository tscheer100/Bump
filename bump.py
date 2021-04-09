#! /usr/bin/env python3


import os
import time
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv
import time


# uncomment the line below if you're trying to edit code in VSCode
os.chdir('./Bump')
load_dotenv('./.env')
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents(members = True, messages = True, guilds = True)

client = commands.Bot(intents = intents, command_prefix = "!", status=discord.Status.online, activity=discord.Game("under construction"))

bumping = False

lock = asyncio.Lock()

@client.event
async def on_ready():
    print("Bump Reminder is now running")

@client.event
async def on_message(message):
    ch = message.channel
    time = 0
    global bumping
    should_bump = False

    if message.author.id == 302050872383242240:
        if message.embeds:
            await lock.acquire()
            try:
                if "done" in message.embeds[0].description:
                    # done statement still needs to be checked.
                    time = 120
                    embed_done = discord.Embed(
                        title = "Bump complete!",
                        color = discord.Colour.purple(),
                        description = "bump again in 2 hours"
                    )
                    await ch.send(embed = embed_done)
                elif "wait" in message.embeds[0].description:
                    desc = message.embeds[0].description
                    time_list = [int(i) for i in desc.split() if i.isdigit()]
                    time = time_list[0]
                    time_conv = str(time_list[0])

                    embed_wait = discord.Embed(
                        title = "Wait to bump",
                        color = discord.Colour.purple(),
                        description = "Bump again in " + time_conv + " minutes"
                    )       
                    await ch.send(embed = embed_wait)
                else:
                    print("desc uncaught") # debug
            finally:
                if bumping == False:
                    should_bump = True
                    bumping = True
                lock.release()
                if should_bump:
                    await asyncio.sleep(time * .060) # time shortened for debug
                    await ch.send("time to bump! waited " + str(time))
                    bumping = False

client.run(DISCORD_TOKEN)
