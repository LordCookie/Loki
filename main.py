import asyncio as asyncio
import discord
import invoke as invoke
from discord import Game, Server, Member, Embed

import SECRETS

client = discord.Client()


@client.event
@asyncio.coroutine
def on_ready():
    print("Bot is logged in successfully. Running on servers:\n")
    for s in client.servers:
        print("  - %s (%s)" % (s.name, s.id))
    yield from client.change_presence(game=Game(name=">_<"))


client.run(SECRETS.TOKEN)