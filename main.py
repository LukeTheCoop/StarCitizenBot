#main.py
import discord
from discord.ext import commands
import info
import asyncio
from time import sleep
import re

client = commands.Bot(command_prefix=".")


temp_dict = {
    'footer': {'text': 'https://www.trackersc.com'}, 
    'thumbnail': 
        {'width': 1200, 'url': 'https://robertsspaceindustries.com/rsi/static/tavern/opengraph.png', 'proxy_url': 'https://images-ext-2.discordapp.net/external/K0M9yjAMK_bAemNNhEB2vg_p0m27AbzMdUGS6b7bh4M/https/robertsspaceindustries.com/rsi/static/tavern/opengraph.png', 'height': 630}, 
    'author': 
        {'url': 'https://www.trackersc.com', 'proxy_icon_url': 'https://images-ext-2.discordapp.net/external/nBfowGy9HcFf3mENC2IbAR16UN3WAqRCPGxAjehbtbw/https/www.trackersc.com/images/website-logo-250.png', 'name': 'Dev Tracker - TrackerSC.com', 'icon_url': 'https://www.trackersc.com/images/website-logo-250.png'}, 
    'type': 'rich', 
    'description': 'Wakapedia-CIG', 
    'url': 'https://robertsspaceindustries.com/spectrum/community/SC/forum/4/thread/weekend-playtest-fleet-week-expo-halls-javelin-tou/4006567', 
    'title': '[Weekend Playtest] Fleet Week, Expo Halls, Javelin Tour, oh my!'}

async def check_update(channel, dict):
    old_update = "" 
    new_update = info.update_news(dict)
    if new_update == None:
    	pass
    else:
    	print('temp')
    	if new_update != old_update:
            old_update = new_update
            await channel.send(new_update)



@client.event 
async def on_ready():
    print(f"Logged on as {client.user}")

@client.event
async def on_message(message):
	print(f'{message.author} said: {message.content}')
	if message.author == client.user:
		return
	else:
		await message.channel.send('...')
		channel = await client.fetch_channel(840432591421440041)
		client.loop.create_task(check_update(channel, temp_dict))


@client.command(name="hi")
async def hi(ctx):
    await ctx.send(f"Hey {ctx.author.mention}")


if __name__ == '__main__':   
	client.run('ODQwMzU5NTY5MDQxNzg0ODQy.YJXD1g.BNd7f58yhpvTA851rS3KILPlzZ4')



	


# Tracker Embed #

# test_embed = discord.Embed(type= 'rich', description ='Wakapedia-CIG', url = 'https://robertsspaceindustries.com/spectrum/community/SC/forum/4/thread/weekend-playtest-fleet-week-expo-halls-javelin-tou/4006567', title = '[Weekend Playtest] Fleet Week, Expo Halls, Javelin Tour, oh my!) #this creates a embed actually')
# test_embed.set_author(url = 'https://www.trackersc.com', name = 'Dev Tracker - TrackerSC.com', icon_url = 'https://www.trackersc.com/images/website-logo-250.png')
# test_embed.set_footer(text='https://www.trackersc.com')
# test_embed.set_thumbnail(url='https://robertsspaceindustries.com/rsi/static/tavern/opengraph.png')
