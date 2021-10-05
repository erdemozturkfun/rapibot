from discord.ext import commands
import discord
import os
import app
import youtubeplayer
from discord import FFmpegPCMAudio
from websrv import keep_alive
import queryfinder

bot = commands.Bot(command_prefix='7')

FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn'}

@bot.command()
async def meme(ctx):

    submission = app.getrandomsubm()
    embed = discord.Embed(title = submission.title, url = "https://www.reddit.com{}".format(submission.permalink))
    footertext = "\N{THUMBS UP SIGN} {upvts}".format(upvts = submission.score)

    embed.set_footer(text=footertext)
    embed.set_image(url=submission.url)
      
    meme = await ctx.send(embed=embed)
    await meme.add_reaction("\N{THUMBS UP SIGN}")

@bot.command()    
async def earth(ctx):
    submission = app.getearthporn()
    embed = discord.Embed(title = submission.title, url = "https://www.reddit.com{}".format(submission.permalink))
    footertext = "Isnt it just beautiful?"

    embed.set_footer(text=footertext)
    embed.set_image(url=submission.url)
      
    await ctx.send(embed=embed)

@bot.command()
async def food(ctx):
      submission = app.getfoodporn()
      embed = discord.Embed(title = submission.title, url = "https://www.reddit.com{}".format(submission.permalink))
      footertext = "yum yum yum"

      embed.set_footer(text=footertext)
      embed.set_image(url=submission.url)
      
      food = await ctx.send(embed=embed)
      await food.add_reaction("<:yummy:895013420754153514>")


@bot.command()
async def play(ctx, url: str):
  
      vc = ctx.author.voice.channel
      voicevideo = youtubeplayer.geturl(url)
      audiosrc = FFmpegPCMAudio(voicevideo.url, **FFMPEG_OPTIONS)    

  
      vclient = await vc.connect()
      vclient.play(audiosrc)
      await ctx.send("Now Playing: " + voicevideo.title)


@bot.command()
async def stop(ctx):
  await ctx.send("Left from the VC.")
  await bot.voice_clients[0].disconnect()

@bot.command()
async def reddit(ctx, subreddit:str,searchquery:str):
  submission = app.searchpost(subredditquery= subreddit,postquery = searchquery)
  embed = discord.Embed(title = submission.title, url = "https://www.reddit.com{}".format(submission.permalink))
  footertext = "\N{THUMBS UP SIGN} {upvts}".format(upvts = submission.score)

  embed.set_footer(text=footertext)
  embed.set_image(url=submission.url)

  await ctx.send(embed = embed)
      
@bot.command()
async def youtube(ctx, searchquery:str):
    vc = ctx.author.voice.channel
    voicevideo = queryfinder.searchyoutube(searchquery)
    audiosrc = FFmpegPCMAudio(voicevideo.url, **FFMPEG_OPTIONS)    

  
    vclient = await vc.connect()
    vclient.play(audiosrc)
    await ctx.send("Now Playing: " + voicevideo.title)



keep_alive()
bot.run(os.environ['BOTTOKEN'])



