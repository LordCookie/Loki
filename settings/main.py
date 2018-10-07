import asyncio as asyncio
import discord
from discord import Game, Embed
from discord.ext.commands import bot

from settings import SECRETS, STATICS
from commands import cmd_ping
from commands import  cmd_help

client = discord.Client()

commands = {

    "ping": cmd_ping,
    "help": cmd_help,
}


@client.event
@asyncio.coroutine
def on_ready():
    print("Bot is logged in successfully. Running on servers:\n")
    for s in client.servers:
        print("  - %s (%s)" % (s.name, s.id))
    yield from client.change_presence(game=Game(name="mit Nekos"))

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

@client.event
@asyncio.coroutine
def on_member_join(member):
    yield from client.send_message(member, "Welcome %s\nin this Paradies full of naughty things.\n\nDon't fap too much" % (member.name))


client.run(SECRETS.TOKEN)