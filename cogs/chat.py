import os
import openai
from discord.ext import commands


OPENAI_KEY = os.getenv("OPENAI_KEY")
openai.api_key = OPENAI_KEY


class Chat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.guild_only()
    @commands.command(name='idea')
    async def idea(self, ctx, *, genre):
        try:
            prompt = f"Generate a unique game idea for a {genre} game. Focus on gameplay mechanics, setting, and a story hook."

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a game design assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=150
            )
            game_idea = response['choices'][0]['message']['content']
            await ctx.send(game_idea)
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")


async def setup(bot):
    await bot.add_cog(Chat(bot))