import discord
from discord.ext import commands
from pytz import timezone
from bot_practice1.core.classes import Cog_Extension
import json
import datetime

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class C_Main(Cog_Extension):
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)')

    @commands.command()
    async def hi(ctx):
        await ctx.sent('Hi~~')

    @commands.command()
    async def help(self, ctx):
        embed=discord.Embed(title="For more info", description="Add rpg before any command", color=0x000000, 
        timestamp=datetime.datetime.now(timezone(datetime.timedelta(hours=+8))))
        embed.set_author(name="Commands", url="" , icon_url="")
        embed.add_field(name="Cold Down", value="Hunt", inline=False)
        embed.set_footer(text="")
        await ctx.send(embed = embed)
      
    @commands.command()
    async def sayd(self, ctx): #訊息複誦
        await ctx.message.delete()

    

def setup(bot):
    bot.add_cog(C_Main(bot))