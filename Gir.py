# Gir bot by Arlix
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk

bot = commands.Bot(command_prefix='!')

print (discord.__version__)

@bot.event
async def on_ready():
    print ("Ready when you are xd")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: ping!! xSSS")
    print ("user has pinged")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0x00ff00)
    embed.set_author(name="Server's Info")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Cya, {}. Ya loser!".format(user.name))
    await bot.kick(user)

@bot.command(pass_context=True)
async def ban(ctx, user: discord.Member):
    await bot.say("Hai.. oh wait BAI".format(user.name))
    await bot.ban(user)

@bot.command(pass_context=True)
async def embed(ctx):
    embed = discord.Embed(title="test", description="my name jeff", color=0x00ff00)
    embed.set_footer(text="this is a footer")
    embed.set_author(name="Jeff")
    embed.add_field(name="This is a field", value="no it isn't", inline=True)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def restart(ctx):
      await bot.say(":wave:")
      await bot.restart

@bot.command(pass_context=True)
async def Hi(ctx):
    await bot.say("Hi world I am a bot and you are a Human")
    print ("I am a bot")

@bot.command(pass_context=True)
async def invite(ctx):
    await bot.say("Use this URL to invite me :ribbon: https://discordapp.com/api/oauth2/authorize?client_id=406998322847416322&permissions=8&scope=bot")
    
bot.run("token")
