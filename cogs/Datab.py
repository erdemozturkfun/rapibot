from discord.ext import commands
import discord
from replit import db

class Datab(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command()
  async def enter(self, ctx, value:str):
    db[ctx.author.discriminator] = value


  @commands.command(name="get")
  async def retrieve(self, ctx):
    if(db[ctx.author.discriminator]):
      value = db[ctx.author.discriminator]
      dm = await ctx.author.create_dm()
      await dm.send(value)



def setup(bot):
  bot.add_cog(Datab(bot))