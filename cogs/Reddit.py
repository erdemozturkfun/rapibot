import discord
import app
from discord.ext import commands
from discord import Colour

class Reddit(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command()
  async def meme(self, ctx):

    submission = app.getrandomsubm()
    embed = discord.Embed(title = submission.title,colour=Colour.red(), url = "https://www.reddit.com{}".format(submission.permalink))
    footertext = "\N{THUMBS UP SIGN} {upvts}".format(upvts = submission.score)
    embed.set_footer(text=footertext)
    
    embed.set_image(url=submission.url)
      
    meme = await ctx.send(embed=embed)
    await meme.add_reaction("\N{THUMBS UP SIGN}")

  @commands.command()    
  async def earth(self, ctx):
    submission = app.getearthporn()
    embed = discord.Embed(title = submission.title, url = "https://www.reddit.com{}".format(submission.permalink),colour=Colour.dark_green())
    footertext = "Isnt it just beautiful?"

    embed.set_footer(text=footertext)
    embed.set_image(url=submission.url)
      
    await ctx.send(embed=embed)

  @commands.command()
  async def food(self, ctx):
      submission = app.getfoodporn()
      embed = discord.Embed(title = submission.title, url = "https://www.reddit.com{}".format(submission.permalink),colour=Colour.orange())
      footertext = "yum yum yum"

      embed.set_footer(text=footertext)
      embed.set_image(url=submission.url)
      
      food = await ctx.send(embed=embed)
      await food.add_reaction("<:yummy:895013420754153514>")



  @commands.command()
  async def reddit(self, ctx, subreddit:str,searchquery:str):
    submission = app.searchpost(subredditquery= subreddit,postquery = searchquery)
    embed = discord.Embed(title = submission.title, url = "https://www.reddit.com{}".format(submission.permalink))
    footertext = "\N{THUMBS UP SIGN} {upvts}".format(upvts = submission.score)

    embed.set_footer(text=footertext)
    embed.set_image(url=submission.url)

    await ctx.send(embed = embed) 



def setup(bot):
  bot.add_cog(Reddit(bot))


  