import discord 
from discord.ext import commands
import Music

cogs = [Music]

client = commands.Bot(command_prefix="!", intents =discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)

client.run("Colocar o token do bot")