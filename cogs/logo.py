from discord.ext import commands
import discord

class Logo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.guild_only()
    @commands.command(name='logo')
    async def send_logo(self, ctx):
        logo_path = './assets/logo.png'
        with open(logo_path, 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)

async def setup(bot):
    await bot.add_cog(Logo(bot))
