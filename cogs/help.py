from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help')
    async def send_help(self, ctx):
        help_message = """
        **Available Commands:**
- `!resources`: Get a list of game development resources.
- `!info`: Get information about the Game Development Unit's vision and goals.
- `!help`: List all available commands.
- `!logo`: Get the unit's logo.
- `!idea <genre>`: Generate a unique game idea for the specified genre.
- `!quote`: Send an inspiring or random game quote.
- `!coinflip`: Flip a coin and get "Heads" or "Tails".
- `!dailyquiz`: Post the daily quiz for users to answer."""
        await ctx.send(help_message)

async def setup(bot):
    await bot.add_cog(Help(bot))
