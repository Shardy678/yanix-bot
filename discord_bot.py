# This example requires the 'message_content' intent.

import os
import discord
import yt_dlp
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# class MyClient(discord.Client):
#     async def on_ready(self):
#         print(f'Logged on as {self.user}!')

#     async def on_message(self, message):
#         print(f'Message from {message.author}: {message.content}')
#         if message.author.bot:
#             return
#         if message.content.startswith("!"):
#             if message.content == "!hello":
#                 await message.channel.send('Hello') 
                

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_message(message):
    author = message.author
    channel = message.channel
    content = message.content

    print(f'{channel}   {author}: {content}')
    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send("Hello")

@bot.command()
async def join(ctx):
    if ctx.author.voice is None:
        await ctx.send("В голосовом канале никого нет")
        return
    voice_channel = ctx.author.voice.channel
    vc = ctx.guild.voice_client
    if vc is not None:
        if vc.channel == voice_channel:
            await ctx.send("Я уже в голосовом канале")
            return
        else:
            await vc.move_to(voice_channel)
            return
    await voice_channel.connect()
    
@bot.command()
async def leave(ctx):
    if ctx.guild.voice_client is None:
        await ctx.send("Я не нахожусь в голосовом канале")
        return
    vc = ctx.guild.voice_client # А если в начале блока обозначить vc, то и не придётся писать полную команду тремя строками выше? Мне надо проверить это
    await vc.disconnect()

@bot.command()
async def play(ctx, url_or_file):
    if ctx.author.voice is None:
        await ctx.send("В голосовом канале никого нет")
        return
    voice_channel = ctx.author.voice.channel
    vc = ctx.guild.voice_client
    if vc is not None:
        if vc.channel == voice_channel:
            return
        else:
            await vc.move_to(voice_channel)
            return
    await voice_channel.connect()

bot.run(TOKEN)