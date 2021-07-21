import discord
import os
import requests

client = discord.Client()
item = requests.get("https://mlb21.theshow.com/apis/items.json?type=mlb_card&page=1")
print(item.json()['items'][0].keys())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    msg = message.content.lower()
    msg_split = msg.split()
    if message.author == client.user:
        return

    if msg.startswith('!stat'):
        if (len(msg_split) < 3) :
          await message.channel.send("Either player or stat missing. Format your message as \"!stat player_name stat_name\"")
        else:
          await message.channel.send(msg_split[1])

client.run(os.getenv('TOKEN'))