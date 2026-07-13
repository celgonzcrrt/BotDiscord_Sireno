import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

# Discord setup
load_dotenv() # loads the .env file
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Create the bot
bot = commands.Bot(command_prefix='s!', intents=intents) # the prefix used will be s!

# *** Handling events
# Default
@bot.event
async def on_ready():
    print("Hola!")

# Member joins
@bot.event
async def on_member_join(member):
    await member.send(f"Bienvenido al server {member.name}")

# Message sent
@bot.event
async def on_message(message):
    if message.author == bot.user: # so that bot doesn't reply to itself
        return
    
    if "mierda" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} no digas eso!!")
    
    await bot.process_commands(message) # mandatory line

# *** Commands
# Say hello
@bot.command()
async def hello(ctx): # s!hello
    await ctx.send(f"Hola {ctx.author.mention}!")

# Add role
@bot.command()
async def assign(ctx): # role must be under bot role in discord
    role = discord.utils.get(ctx.guild.roles, name="PSOE")
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f"{ctx.author.mention} ahora tiene el rol PSOE")
    else:
        await ctx.send("El rol no existe")

# Remove role
@bot.command()
async def remove(ctx):
    role = discord.utils.get(ctx.guild.roles, name="PSOE")
    if role:
        await ctx.author.remove_roles(role)
        await ctx.send(f"{ctx.author.mention} ya no tiene el rol PSOE")
    else:
        await ctx.send("El rol no existe")

# Secret command if you have psoe
@bot.command()
@commands.has_role("PSOE")
async def secret(ctx):
    await ctx.send("Rojo")
@secret.error
async def secret_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("no tienes permiso")

# Send DM
async def dm(ctx, *, msg):
    await ctx.author.send(f"You said {msg}")

# Direct reply to command
@bot.command()
async def reply(ctx):
    await ctx.reply("esta es una respuesta a tu mensaje")
    
# Create embeded/poll
@bot.command()
async def poll(ctx, *, question):
    embed = discord.Embed(title="New poll", description=question)
    poll_message = await ctx.send(embed=embed)
    await poll_message.add_reaction("👍")
    await poll_message.add_reaction("👎")

# *** Run the bot
bot.run(token, log_handler=handler)   