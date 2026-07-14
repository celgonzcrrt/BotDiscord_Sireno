import discord
from discord.ext import commands

# TODO mejorar el startup
def ready(bot):
    @bot.event
    async def on_ready():
        print("Sireno bot listo para funcionar!")