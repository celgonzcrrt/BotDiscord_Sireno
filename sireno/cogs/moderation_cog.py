import logging
import discord
from discord.ext import commands

logger = logging.getLogger(__name__)

import discord
from discord.ext import commands

class ModerationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # Elimina n mensajes en un canal, reason=razon por la que se eliminan
    @commands.hybrid_command(name="purge", help="Borra N mensajes")
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, n: int, reason: str | None = "No se dio razón"):
        await ctx.defer()
        
        await ctx.channel.purge(limit=n+1, reason=reason)
        await ctx.send(f'Se borraron {n} mensajes por: {reason}')
    
    # Expulsa a un miembro sin banearlo
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, reason: str | None = "No se dio razón"):
        await member.kick(reason=reason)
        await ctx.send(f'El usuario {member} ha sido expulsado por: {reason}')
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.reply("No tienes los permisos para hacer esto :)")
            
    # Banear un usuario
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, reason: str | None = "No se dio razón"):
        await member.ban(reason=reason)
        await ctx.send(f'El usuario {member} ha sido baneado por: {reason}')
    @ban.error 
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.reply("No tienes permisos para hacer esto :)")
    
    # Dar rol
    @commands.command(name="darRol")
    @commands.has_permissions(manage_roles=True)
    async def darRol(self, ctx, member: discord.Member, *, role: str):
        await member.add_roles(discord.utils.get(ctx.guild.roles, name=role))
        await ctx.send(f'{member} ahora tiene el rol {role}!')
    @darRol.error
    async def darRol_error(self, ctx, error):
        if isinstance(error, commands.RoleNotFound):
            await ctx.reply("El rol que tratas de dar no existe, revisa el nombre")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.reply("No tienes permisos para realizar esta acción")
        else:
            await ctx.reply("equisde")
            
    # Borrar rol
    @commands.command(name="quitarRol")
    @commands.has_permissions(manage_roles=True)
    async def quitarRol(self, ctx, member: discord.Member, role: str):
        await member.remove_roles(discord.utils.get(ctx.guild.roles, name=role))
        await ctx.send(f'{member} ya no tiene el rol {role}')
    @quitarRol.error
    async def quitarRol_error(self, ctx, error):
        if isinstance(error, commands.RoleNotFound):
            await ctx.reply("El rol no existe, revisa el nombre")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.reply("No tienes permiso para realizar esta acción")
        else:
            await ctx.reply("equisde")

# Añadir al cog
async def setup(bot: commands.Bot):
    await bot.add_cog(ModerationCog(bot))