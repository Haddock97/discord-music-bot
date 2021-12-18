import os

import discord
from discord.ext import commands

TOKEN = os.environ['DISCORD_TOKEN']

bot = commands.Bot(command_prefix='.')
@bot.command()
async def play(ctx):
    await ctx.send('Play song here')
bot.run(TOKEN)
