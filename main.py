import discord
import os
from StatFinder import findStat

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    msg = message.content.lower()
    msg_split = msg.split()
    if message.author == client.user:
        return

    #find player specific stat
    if msg.startswith('!stat'):
      returnList = findStat(msg_split, message)
      if (returnList != []):
        for x in returnList:
          await message.channel.send(x)
                

client.run(os.getenv('TOKEN'))