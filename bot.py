import os
import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from dotenv import load_dotenv
import openai
import AI

load_dotenv("TOKENS.env")

BOT_TOKEN = os.getenv("DISCORD_TOKEN")
openai.api_key = os.getenv("AI_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord.')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error

@bot.command()
async def image(ctx, *, arg=None):

    if arg == None:
        return

    await ctx.reply(f'Generating image of "{arg}", one moment...')

    await ctx.reply(AI.create_image(arg))

@bot.command()
async def story(ctx, *, arg=None):

    if arg == None:
        return

    await ctx.reply('Generating story, one moment...')

    await ctx.reply(AI.create_story(arg))

# TOKEN
bot.run(BOT_TOKEN)
    