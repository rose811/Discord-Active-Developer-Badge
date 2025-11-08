import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f'봇이 로그인 됨: {bot.user}')

@bot.command()
async def 섹(ctx):
    await ctx.send(f'스')

# 여기에 니 봇 토큰 넣으면 됨 
bot.run("Token")
