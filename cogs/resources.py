from discord.ext import commands

class Resources(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.guild_only()
    @commands.command(name='resources')
    async def send_resources(self, ctx):
        resources_list = """
        Here are some useful game development assets:
        - Unity Asset Store: https://assetstore.unity.com/
        - OpenGameArt: https://opengameart.org/
        - Kenney Assets: https://kenney.nl/assets
        - Itch.io Assets: https://itch.io/game-assets
        """
        await ctx.send(resources_list)

async def setup(bot):
    await bot.add_cog(Resources(bot))
