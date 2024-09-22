import discord
from discord.ext import commands
import datetime

class DailyQuiz(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.current_quiz = None
        self.correct_answer = None
        self.quiz_time = None
        self.channel_id = 1287148847876931696
        self.answered_users = set()

    # Post the daily quiz in a public channel
    @commands.guild_only()
    @commands.command(name='dailyquiz')
    async def post_daily_quiz(self, ctx):
        if self.current_quiz and self.quiz_time == datetime.date.today():
            await ctx.send(f"Today's quiz has already been posted!")
        else:
            # Set today's quiz and correct answer (change this daily)
            self.current_quiz = """Which Overwatch 2 character says, "I'm the last one you'll ever cross?" """
            self.correct_answer = "Ashe"
            self.quiz_time = datetime.date.today()
            self.answered_users = set()

            await ctx.send(f"📜 **Daily Quiz**: {self.current_quiz}\n\nDM me:\n**!answer <your answer>**\nto avoid spoilers!")

    # Handle user answers in DM
    @commands.command(name='answer')
    async def receive_answer(self, ctx, *, user_answer: str):
        if isinstance(ctx.channel, discord.DMChannel):  # Ensure it's a DM
            if not self.current_quiz:
                await ctx.send("No active quiz. Please wait for the next daily quiz!")
            elif ctx.author.id in self.answered_users:
                await ctx.send("You've already submitted an answer for today's quiz. Try again tomorrow!")
            else:
                if user_answer.lower().strip() == self.correct_answer.lower().strip():
                    # Get the display name of the user
                    user_display_name = ctx.author.display_name

                    # Send a message to the specific server channel
                    channel = self.bot.get_channel(self.channel_id)
                    if channel:
                        await channel.send(
                            f"🎉 Congratulations to **{user_display_name}** for answering the daily quiz correctly!")

                    # Send confirmation to the user in DM
                    await ctx.send("🎉 Correct! Well done!")
                else:
                    await ctx.send("❌ Incorrect. Try again tomorrow!")

                # Add the user to the set of users who have answered
                self.answered_users.add(ctx.author.id)
        else:
            await ctx.send("Please DM me your answer to avoid spoilers.")


async def setup(bot):
    await bot.add_cog(DailyQuiz(bot))
