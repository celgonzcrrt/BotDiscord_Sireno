import discord
from discord.ext import commands

def member_join(bot):
    @bot.event
    async def on_member_join(member):
        await member.send(f"Bienvenido al server {member.name}")