import os
import discord
import app
from websrv import keep_alive

client = discord.Client()


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

keep_alive()
client.run(os.environ['BOTTOKEN'])

