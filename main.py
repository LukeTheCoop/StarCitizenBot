#main.py
import discord
from discord.ext import commands
import info
import asyncio

client = commands.Bot(command_prefix=".")


async def new_article_check(channel):
    old_link = ""    
    while True:
        if info.new_article() == None:
            pass
        else:
            if info.new_article() != old_link:
                old_link = info.new_article()
                await channel.send(info.new_article())
        await asyncio.sleep(10)


@client.event 
async def on_ready():
    print(f"Logged on as {client.user}")
    channel = await client.fetch_channel(840362634846535691)
    client.loop.create_task(new_article_check(channel))



@client.command(name="hi")
async def hi(ctx):
    await ctx.send(f"Hey {ctx.author.mention}")
client.run('ODQwMzU5NTY5MDQxNzg0ODQy.YJXD1g.FZnzR8tVHb-fawLY0esBbybFaT8')



	


# Tracker Embed #

# test_embed = discord.Embed(type= 'rich', description ='Wakapedia-CIG', url = 'https://robertsspaceindustries.com/spectrum/community/SC/forum/4/thread/weekend-playtest-fleet-week-expo-halls-javelin-tou/4006567', title = '[Weekend Playtest] Fleet Week, Expo Halls, Javelin Tour, oh my!) #this creates a embed actually')
# test_embed.set_author(url = 'https://www.trackersc.com', name = 'Dev Tracker - TrackerSC.com', icon_url = 'https://www.trackersc.com/images/website-logo-250.png')
# test_embed.set_footer(text='https://www.trackersc.com')
# test_embed.set_thumbnail(url='https://robertsspaceindustries.com/rsi/static/tavern/opengraph.png')
