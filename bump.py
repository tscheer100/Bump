#! /usr/bin/env python3
import os
import time
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv
import time

# uncomment the line below if you're trying to edit code in VSCode
# os.chdir('./Bump')
load_dotenv('./.env')
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents(members = True, messages = True, guilds = True)

client = commands.Bot(intents = intents, command_prefix = "!d", status=discord.Status.online, activity=discord.Game("under construction") )

bumping = False

lock = asyncio.Lock()

@client.event
async def on_ready():
    print("Bump Reminder is now running")

@client.command(aliases = ['git', 'code'])
async def github(ctx):
    embed = discord.Embed(
        title = "Check out the developer's code!",
        color = discord.Colour.purple(),
    )
    embed.set_thumbnail(url = "https://www.sferalabs.cc/wp-content/uploads/github-logo-white.png")
    embed.add_field(name = "Bump bot code", value = "https://github.com/tscheer100/Bump", inline = False)
    embed.add_field(name = "Developers Github", value = "https://github.com/tscheer100")
    embed.add_field(name = "Support more free bots by paying for the developer's coffee :woozy_face::coffee:", value = "https://www.paypal.com/paypalme/TheTurtleKing", inline = False)
    await ctx.send(embed = embed)    

@client.event
async def on_message(message):
    ch = message.channel
    user = message.author
    time = 0
    global bumping
    should_bump = False

    if message.author.id == 302050872383242240: # <-- this is the ID to disboard
        if message.embeds:
            await lock.acquire()
            try:
                if "done" in message.embeds[0].description:
                    time = 120
                    embed_done = discord.Embed(
                        title = "Bump complete!",
                        color = discord.Colour.purple(),
                        description = "bump again in 2 hours"
                    )
                    embed_done.set_thumbnail(url = "https://media.giphy.com/media/lTjXSsPmX3Jdx4J7DU/giphy.gif")
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
                    embed_wait.set_thumbnail(url = "https://media.giphy.com/media/lTjXSsPmX3Jdx4J7DU/giphy.gif")   
                    await ch.send(embed = embed_wait)
                else:
                    print("desc uncaught") # debug
            finally:
                if bumping == False:
                    should_bump = True
                    bumping = True
                lock.release()
                if should_bump:
                    await asyncio.sleep(time * 60) # time shortened for debug
                    embed_bump = discord.Embed(
                        title = "Time to bump!",
                        color = discord.Colour.purple(),
                        description = "time to bump! Type `!d bump` to bump the server again",
                    )
                    embed_bump.set_footer(url = "https://upload.wikimedia.org/wikipedia/commons/7/7a/Alarm_Clock_GIF_Animation_High_Res.gif")
                    bumping = False
    await client.process_commands(message)

client.run(DISCORD_TOKEN)
