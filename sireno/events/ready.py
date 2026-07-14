import discord
from discord.ext import commands
import os

# TODO mejorar el startup
def ready(bot):
    @bot.event
    async def on_ready():
        # Cargar cogs
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py") and filename != "__init__.py":
                await bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"Se cargó {filename[:-3]}")
        
        print("Sireno bot listo para funcionar!")