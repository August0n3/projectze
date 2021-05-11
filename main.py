import discord 
import asyncio
import sqlite3
from discord.ext import commands
import random
from discord.ext.commands import AutoShardedBot, when_mentioned_or
#comenta ai dps pra eu entender quando eu for ler, se possivel

#definições gerais
client = commands.Bot(command_prefix = "<", case_insensitive = True)

modulos = ["cogs.comando"]

#mensagem inical do bot
@client.event
async def on_ready():
    print('Bot online - Olá, Mundo!')
    # isso aq inicia a stream, ainda n sei mt bem como funciona mas tinha no tutorial
    await client.change_presence(activity=discord.Streaming(name="<help", url="https://www.twitch.com/123"))
    print(client.user)

#iniciador de módulos
#o nome do arquivo dentro de cogs tava diferente. Tava "comandos" mas é pra ser "comando".
if __name__ == "__main__":
    for modulo in modulos:
        client.load_extension(modulo)

    client.run("ODQwMDU1MDk1OTcwMjM0Mzk5.YJSoRg.Pr6dv_758lzs9s-INR6oeOAFGV0")
    # o erro ta sendo na construção do embed agr, mas acho que sei como resolver