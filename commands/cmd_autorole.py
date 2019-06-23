import os
from os import path

import discord

def error(content, channel, client):
    yield from client.send_message(channel, embed=discord.Embed(color=discord.Color.red(), description=content))

def get(server):
    f = "server_settings/" + server.id + "autorole"
    if path.isfile(f):
        with open(f) as f:
            return discord.utils.get(server.roles, id=f.read())
    else:
        return None



def saveFile(id, server):
    if not path.isdir("server_settings/" + server.id):
        os.makedirs("server_settings/"+ server.id)
    with open("server_settings/" + server.id + "/autorole", "w") as f:
        f.write(id)
        f.close()

def ex(args, message, client, invoke):

    print(args)

    if len(args) > 0:
        rolename = args.__str__()[1:-1].replace(",", "").replace("'", "")
        role = discord.utils.get(message.server.roles, name=rolename)
        if role == None:
            yield from error("Hey coward .... can you please enter a Valid Role this annoy me \n\n\n .... Baka ^^", message.channel, client)
        else:
            try:
                saveFile(role.id, message.server)
                yield from client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description=("Finally you made it( ︶︿︶) you are now a `%s`" % role.name)))
            except Exception:
                yield from error("WRONG .... Idiot", message.channel, client)
                raise Exception