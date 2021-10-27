from discord.ext import commands
import discord
import os
from discord import Colour
from websrv import keep_alive
from replit import db


intents = discord.Intents.all()
bot = commands.Bot(command_prefix='7', intents=intents)

FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn'}

@bot.event
async def on_ready():
 activity = discord.Game("meraba")
 await bot.change_presence(status=discord.Status.dnd, activity=activity)






      
bot.load_extension('cogs.Datab')
bot.load_extension('cogs.Youtube')
bot.load_extension('cogs.Reddit')
keep_alive()
bot.run(os.environ['BOTTOKEN'])



