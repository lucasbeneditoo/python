import os
import discord
import asyncio
import random
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot online como {bot.user}!")

@bot.command(
        help="Responde de volta com Pong!"
)
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command(
    aliases=["r", "dado", "rolar"],
    help="Rola um dado de 6 lados."
)
async def roll(ctx):
    dado = random.randint(1, 6)
    await ctx.send("Você rolou o dado!")
    await asyncio.sleep(0.5)
    await ctx.send("...")
    await asyncio.sleep(0.5)
    await ctx.send(f"Caiu no número {dado}!")
    
bot.run(TOKEN)
