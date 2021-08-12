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

    if msg.startswith('!help'):
      await message.channel.send("Welcome to the Show Bot. Here is a guide to the current commands.\n!stat player_name series_name stat_name: type !stat followed by a player name, their card's series name, and a stat name to find out any stat from any card!\n!stat stats_list: gives a list of all possible stat keywords\nMore commands will be added in the future so stay tuned!")
                

client.run(os.getenv('TOKEN'))