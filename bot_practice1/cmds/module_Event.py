import discord
from discord.ext import commands
from discord.ext.commands.core import command
from bot_practice1.core.classes import Cog_Extension
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)
    
class C_Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata['BeginChannel']))
        await channel.send(f'{member} join!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata['BeginChannel']))
        await channel.send(f'{member} leave :\'(')
    
    @commands.Cog.listener()
    async def on_message(self, msg): #不須prefix也會觸發
        if msg.content in jdata['keyword'] and msg.author != self.bot.user:
            await msg.channel.send('1min cooldown')

def setup(bot):
    bot.add_cog(C_Event(bot))