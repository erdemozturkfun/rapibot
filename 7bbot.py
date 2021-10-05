import os
import discord
import app
import youtubeplayer
from websrv import keep_alive
from discord import FFmpegPCMAudio, PCMVolumeTransformer


client = discord.Client()
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn'}

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):


    if message.author == client.user:
        return

    if message.content.startswith('7b meme'):
      submission = app.getrandomsubm()
      embed = discord.Embed(title = submission.title, url = "https://www.reddit.com{}".format(submission.permalink))
      footertext = "\N{THUMBS UP SIGN} {upvts}".format(upvts = submission.score)

      embed.set_footer(text=footertext)
      embed.set_image(url=submission.url)
      
      await message.channel.send(embed=embed)
    elif message.content.startswith('7b earth'):
      submission = app.getearthporn()
      embed = discord.Embed(title = submission.title, url = "https://www.reddit.com{}".format(submission.permalink))
      footertext = "Isnt it just beautiful?"

      embed.set_footer(text=footertext)
      embed.set_image(url=submission.url)
      
      await message.channel.send(embed=embed)
    elif message.content.startswith('7b food'):
      submission = app.getfoodporn()
      embed = discord.Embed(title = submission.title, url = "https://www.reddit.com{}".format(submission.permalink))
      footertext = "yum yum yum"

      embed.set_footer(text=footertext)
      embed.set_image(url=submission.url)
      
      await message.channel.send(embed=embed)
    elif message.content.startswith("7b play") :
      url = message.content[7:]
      vc = message.author.voice.channel
      audiosrc = FFmpegPCMAudio(youtubeplayer.geturl(url), **FFMPEG_OPTIONS)    

  
      vclient = await vc.connect()
      vclient.play(audiosrc)
    elif message.content.startswith("7b stop"):
      await client.voice_clients[0].disconnect()



keep_alive()
client.run(os.environ['BOTTOKEN'])

