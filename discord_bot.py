import os
import discord
import yt_dlp
from discord.ext import commands
from dotenv import load_dotenv
from discord import FFmpegPCMAudio

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise ValueError("DISCORD_TOKEN отсутствует в .env")

ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": "%(extractor)s-%(id)s-%(title)s.%(ext)s",
    "restrictfilenames": True,
    "noplaylist": True,
    "nocheckcertificate": True,
    "ignoreerrors": False,
    "default_search": "auto",
    "source_address": "0.0.0.0",
    "no_warnings": True,
    "js_runtimes": {"node": {}},
}


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_message(message):
    author = message.author
    channel = message.channel
    content = message.content

    print(f"[{channel}] {author}: {content}")
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
    vc = ctx.guild.voice_client
    if vc is None:
        await ctx.send("Я не нахожусь в голосовом канале")
        return
    await vc.disconnect()


@bot.command()
async def play(ctx, url_or_file=None):
    if url_or_file is None:
        await ctx.send("Дай мне ссылку")
        return

    if ctx.author.voice is None:
        await ctx.send("В голосовом канале никого нет")
        return

    voice_channel = ctx.author.voice.channel
    vc = ctx.guild.voice_client
    if vc is not None:
        if vc.channel == voice_channel:
            pass
        else:
            await vc.move_to(voice_channel)
    else:
        vc = await voice_channel.connect()

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url_or_file, download=False)
        audio_url = info["url"]

    source = FFmpegPCMAudio(audio_url)
    vc.play(source)


bot.run(TOKEN)
