import discord
from discord.ext import commands
from bot_practice1.core.classes import Cog_Extension
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class C_React(Cog_Extension):
    @commands.command()
    async def hunt(self, ctx):
        await ctx.sent('1min CD')

def setup(bot):
    bot.add_cog(C_React(bot))