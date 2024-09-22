import random
from discord.ext import commands

class CoinFlip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.guild_only()
    @commands.command(name='coinflip')
    async def coinflip(self, ctx):
        outcome = random.choice(["Heads", "Tails"])
        await ctx.send(f"The coin landed on: {outcome}")

async def setup(bot):
    await bot.add_cog(CoinFlip(bot))
