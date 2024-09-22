from discord.ext import commands
import random

class Quote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.guild_only()
    @commands.command(name='quote')
    async def quote(self, ctx):
        quotes = [
            '**"The best games are made by those who play them."**',
            '**"Innovation comes from those who are not afraid to fail."**',
            '**"Every game is a journey, and every journey has a story."**',
            '**"Hesitation is defeat."**\n— *Isshin Ashina*',
            '**"YOU DIED"**\n— *Dark Souls*',
            '**"Praise the sun!"**\n— *Solaire of Astora, Dark Souls*',
            '**"In the midst of chaos, there is also opportunity"**\n— *Sun-Tzu, The Art of War*',

        ]
        await ctx.send(random.choice(quotes))

async def setup(bot):
    await bot.add_cog(Quote(bot))
