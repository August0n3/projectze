import discord 
from discord.ext import commands
from discord.ext.commands import AutoShardedBot, when_mentioned_or

#definições gerais
client = commands.Bot(command_prefix = "<", case_insensitive = True)

modulos = ["cogs.comando"]

#mensagem inical do bot
@client.event
async def on_ready():
    print('Bot online - Olá, Mundo!')
    # isso aq inicia a stream
    await client.change_presence(activity=discord.Streaming(name="<help", url="https://www.twitch.com/123"))
    print(client.user)

#iniciador de módulos e token
if __name__ == "__main__":
    for modulo in modulos:
        client.load_extension(modulo)

    client.run("****")#colocar a chave de inicio do discord.
