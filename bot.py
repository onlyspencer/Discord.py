import discord
from discord.ext import commands
  
bot = commands.Bot(command_prefix = "", description = "")
# command_prefix = "enter your prefix"
# description = "description of bot"

# Ping command
@bot.command()
async def ping(ctx):
  print("pong !")
     await ctx.send("pong !")
    

# Server info command
@bot.command()
async def serverinfo(ctx):
  server = ctx.guild
  
  numberOfTextChannels = len(server.text_channels)    # Settings the number of text channels
  numberOfVoiceChannels = len(server.voice_channels)  # Settings the number of voice channels
  serverDescription = server.description              # Settings the server's description
  numberOfPerson = server.member_count                # Settings the number of members
  serName = server.name                               # Settings the server's name
  
  message = "This server (`serName`), content `{numberOfTextChannels}` voice channels and `{numberOfTextChannels}` text channels \n The serveur's description is : '`{serverDescription}`' \n They are `{numberOfPerson} !`"

  
bot.run('') # Enter here your bot's token
