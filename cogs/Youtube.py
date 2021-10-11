import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import youtubeplayer
import queryfinder

FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn'}

class Youtube(commands.Cog):
 def __init__(self, bot):
  self.bot = bot

 @commands.command()
 async def play(self, ctx, url: str):
  
  vc = ctx.author.voice.channel
  voicevideo = youtubeplayer.geturl(url)
  audiosrc = FFmpegPCMAudio(voicevideo.url, **FFMPEG_OPTIONS) 

  


  vclient = await vc.connect()
  vclient.play(audiosrc)
  await ctx.send("Now Playing: " + voicevideo.title)

 @commands.command()
 async def stop(self, ctx):
  await ctx.send("Left from the VC.")
  await self.bot.voice_clients[0].disconnect()

 @commands.command()
 async def pause(self, ctx):
  if self.bot.voice_clients[0].is_paused():
   await ctx.send("Already Paused")
  else:
   self.bot.voice_clients[0].pause()
    
 @commands.command()
 async def contin(self, ctx):

  if self.bot.voice_clients[0].is_playing():
   await ctx.send("Already Playing!")
  else:
   self.bot.voice_clients[0].resume()

 @commands.command()
 async def youtube(self, ctx, searchquery:str):
    vc = ctx.author.voice.channel
    voicevideo = queryfinder.searchyoutube(searchquery)
    audiosrc = FFmpegPCMAudio(voicevideo.url, **FFMPEG_OPTIONS)    

  
    vclient = await vc.connect()
    vclient.play(audiosrc)
    await ctx.send("Now Playing: " + voicevideo.title)

def setup(bot):
 bot.add_cog(Youtube(bot))
