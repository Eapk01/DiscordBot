from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='info')
    async def send_info(self, ctx):
        info_message = """
**Game Development Unit Information:**
- **Vision:** To foster a collaborative environment for learning and creating games.
- **Goals:** 
    1. Enhance game development skills through projects and workshops.
    2. Promote creativity and teamwork.
    3. Organize game jams and competitions (I think...).
- **Join us**: Get involved in our game projects, study groups, or show off your own games!
        """
        await ctx.send(info_message)

async def setup(bot):
    await bot.add_cog(Info(bot))
