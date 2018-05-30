import asyncio as asyncio
import discord
from discord import Game, Server, Member, Embed

import SECRETS
import STATICS
import cmd_ping

client = discord.Client()

commands = {

    "ping": cmd_ping,

}


@client.event
@asyncio.coroutine
def on_ready():
    print("Bot is logged in successfully. Running on servers:\n")
    for s in client.servers:
        print("  - %s (%s)" % (s.name, s.id))
    yield from client.change_presence(game=Game(name=">_<"))

@client.event
@asyncio.coroutine
def on_message(message):
    print(message.content + " - " + message.author.name)
    if message.content.startswith(STATICS.PREFIX):
        invoke = message.content[len(STATICS.PREFIX):].split(" ")[0]
        args = message.content.split(" ")[1:]
        print("INVOKE: %s\nARGS: %s" % (invoke, args.__str__()[1:-1].replace("'", "")))
        if commands.__contains__(invoke):
            yield from commands.get(invoke).ex(args, message, client, invoke)
        else:
            yield from client.send_message(message.channel, embed=Embed(color=discord.Color.red(), description="`%s` don't exist!" % invoke))

client.run(SECRETS.TOKEN)