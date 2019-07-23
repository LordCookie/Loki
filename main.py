import asyncio as asyncio
import discord
from discord import Game, Embed
from discord.ext.commands import bot

from settings import SECRETS, STATICS
from commands import cmd_ping
from commands import cmd_help
from commands import cmd_autorole

client = discord.Client()

commands = {

    "ping": cmd_ping,
    "help": cmd_help,
    "autorole": cmd_autorole,

}


@client.event
async def on_ready():
    print("Bot is logged in successfully. Running on servers:\n")
    for s in client.servers:
        print("  - %s (%s)" % (s.name, s.id))
    await client.change_presence(game=Game(name="mit Nekos"))

@client.event
async def on_message(message):
    print("'" + message.content + "'" + " From : " + message.author.name)
    if message.content.startswith(STATICS.PREFIX):
        invoke = message.content[len(STATICS.PREFIX):].split(" ")[0]
        args = message.content.split(" ")[1:]
        print("INVOKE: %s\nARGS: %s" % (invoke, args.__str__()[1:-1].replace("'", "")))
        print("Command" + "..." + "was executet sucsessfully.")
        if commands.__contains__(invoke):
            await commands.get(invoke).ex(args, message, client, invoke)
        else:
            await client.send_message(message.channel, embed=Embed(color=discord.Color.red(), description="`%s` don't exist!" % invoke))


@client.event
async def on_member_join(member):
    await client.send_message(member, "Welcome %s\nin this Paradies full of naughty things.\n\nDon't fap too much" % (member.name))

    #role = discord.utils.get(member.server.roles, id='592392234922672165')
    role = cmd_autorole.get(member.server, id)                                                                    #idk müsste eigentlich so passen aber der hat wohl probleme beim übergeben der ID(rolen name)
    await client.add_roles(member, role)


    """role = cmd_autorole.get(member.server)
    if role is not None:
        await client.add_roles(member, role)
        try:
            await client.send_message(member, "Hey I tought you look Like an " + role.name + "!!")
        except Exception:
           await client.send_message(member, "You have no Role!")
           raise Exception"""



client.run(SECRETS.TOKEN)