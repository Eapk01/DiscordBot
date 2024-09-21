from discord.ext import commands

class Secrets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='nullpo')
    async def quote(self, ctx):
        await ctx.send("GAH!!")

async def setup(bot):
    await bot.add_cog(Secrets(bot))
