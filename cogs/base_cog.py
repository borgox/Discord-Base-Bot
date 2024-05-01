from disnake.ext import commands
import disnake

class Test(commands.Cog):
    def __init__(self, bot:commands.InteractionBot):
        self.bot = bot
    
    @commands.slash_command(description="test command!")
    async def test(inter:disnake.ApplicationCommandInteraction, text:str):
        await inter.response.send_message(f"You said: {text}!")


def setup(bot):
    bot.add_cog(Test(bot))