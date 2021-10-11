from discord.ext import commands
import discord
import os
from discord import Colour
from websrv import keep_alive



intents = discord.Intents.all()
bot = commands.Bot(command_prefix='7', intents=intents)

FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn'}

@bot.event
async def on_ready():
 activity = discord.Game("meraba")
 await bot.change_presence(status=discord.Status.dnd, activity=activity)



@bot.command()
async def test(ctx):
  mentions = ctx.message.mentions
  activ = mentions[0].activity
 
  if activ == None:
      await ctx.send("No activity!")
  else:
    if isinstance(activ, discord.Spotify):
      embed = discord.Embed(title= "Mention listens to: " + activ.title, description = "in " + activ.album,url=activ.album_cover_url, colour=activ.colour)
      embed.set_thumbnail(url=activ.album_cover_url)
      embed.set_author(name="by " + activ.artist)
      await ctx.send(embed=embed)
    elif isinstance(activ, discord.CustomActivity):
      await ctx.send("Mention is doing " + activ.name)
    else:  
      embed = discord.Embed(title= "Mention plays: " + activ.name, colour = Colour.dark_blue())
      if activ.small_image_url != None:
        embed.set_footer(text=activ.small_image_text,icon_url=activ.small_image_url)
        await ctx.send(embed=embed)
      else:
        embed.set_footer(text=activ.large_image_text,icon_url=activ.large_image_url)
        await ctx.send(embed=embed)
      
        

      

bot.load_extension('cogs.Youtube')
bot.load_extension('cogs.Reddit')
keep_alive()
bot.run(os.environ['BOTTOKEN'])



