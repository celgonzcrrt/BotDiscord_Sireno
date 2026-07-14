import logging

logger = logging.getLogger(__name__)

import discord
from discord.ext import commands

class ModerationCog(commands.Cog, name="Moderacion", description="Comandos para moderadores"):
    def __init__(self, bot):
        self.bot = bot
    
    # Elimina n mensajes en un canal, reason=razon por la que se eliminan
    @commands.command
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, n: int, reason: str | None = "No se dio razón"):
        await ctx.defer()
        
        await ctx.channel.purge(limit=n+1, reason=reason)
        await ctx.send(f'Se borraron {n} mensajes por: {reason}')

# Añadir al cog
async def setup(bot: commands.Bot):
    await bot.add_cog(ModerationCog(bot))