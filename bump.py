#! /usr/bin/env python3


import os
import time
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv


# uncomment the line below if you're trying to edit code in VSCode
# os.chdir('./Bump')
load_dotenv('./.env')
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents(members = True, messages = True, guilds = True)

client = commands.Bot(intents = intents, command_prefix = "!t ", status=discord.Status.online, activity=discord.Game("under construction"))

@client.event
async def on_ready():
    print("Bump Reminder is now running")

@client.event
async def on_message(message):
    ch = message.channel

    if message.author.id == 302050872383242240: # <---- this number is the Disboard user ID

        await ch.send("bump called")
        if message.embeds:
            await ch.send("embed")

            if "done" in message.embeds[0].description:
                await ch.send("bump success, starting timer for 120 minutes")
                await asyncio.sleep(7200)
                await ch.send("Time to bump.")
            elif "wait" in message.embeds[0].description:
                desc = message.embeds[0].description
                num = [int(i) for i in desc.split() if i.isdigit()]
                num_conv = str(num[0])
                print(num)
                await ch.send("bump wait " + num_conv + " minutes")
                await asyncio.sleep(num[0] * 60)
                await ch.send("time to bump again!")
            else:
                await ch.send("desc uncaught")
                print("nothing found")
    await client.process_commands(message)


    
client.run(DISCORD_TOKEN)
