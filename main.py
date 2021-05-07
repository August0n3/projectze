import discord 
import asyncio
from models.streamer import Streamer

client = discord.Client()

cor= '#39CACF'

@client.event
async def on_ready():
    print('Bot online - Olá, Mundo!')
    print(client.user)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('<help'):
        embed = discord.Embed(
            title= 'Bem vindo ao José bot! O bot que simula a vida de um streamer!',
            description="Para registrar-se digite - <register \n"
                        "Para ir para a loja digite - <store\n"
                        "Para ver seus status digite - <status\n"
                        "Para começar uma stream digite- <stream\n"
        )
    botmsg= await message.channel.send(embed=embed)


client.run('ODQwMDU1MDk1OTcwMjM0Mzk5.YJSoRg.Pr6dv_758lzs9s-INR6oeOAFGV0')