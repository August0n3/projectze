import discord 
import asyncio
import sqlite3
from models.streamer import Streamer
from models.streamerDAO import StreamerDAO

database= 'database/projectze.db'
conect =sqlite3.connect(database)

client = discord.Client()

#criando o embed da mensagem <help
help_embed = discord.Embed(
            title= 'Bem vindo ao José bot! O bot que simula a vida de um streamer!',
            color=3787471,
            description="Para registrar-se digite - <register \n"
                        "Para ir para a loja digite - <store\n"
                        "Para ver seus status digite - <status\n"
                        "Para começar uma stream digite- <stream\n"
        )
#definindo a imagem do embed help
help_embed.set_image(url='https://imgur.com/ELbZ9aM.png')

msg_id = None
msg_user = None

#mensagem inical do bot
@client.event
async def on_ready():
    print('Bot online - Olá, Mundo!')
    print(client.user)

@client.event
async def on_message(message):
    #criando a mensagem de <help
    if message.content.lower().startswith('<help'):
        global help_embed
        help_msg = await message.channel.send(embed=help_embed)

    #criando register
    if message.content.lower().startswith("<register"):
        streamerDAO=StreamerDAO(conect)
        idstreamer = int(message.author.id)
        namestreamer = str(message.author)
        streamer=Streamer(
            idstreamer,
            namestreamer,
            0,
            50,
            0,
            1000
            ) 
        streamerDAO.cadastro(streamer)
        if streamer.id != None:
            await message.channel.send("Cadastrado com sucesso!")
        else:
            await message.channel.send('Falha no cadastro.')
#não esta funcionando 
@client.event
async def on_member_join(member):
  canal = client.get_channel("840059515462090824")
  msg = "Bem Vindo {}".format(member.mention)
  await client.send(canal, msg) 

@client.event
async def on_member_remove(member):
   canal = client.get_channel("840059515462090824")
   msg = "Adeus garotinho juvenil {}".format(member.mention)
   await client.channel.send(canal, msg) #substitua canal por member para enviar a msg no DM do membro

#iniciando o bot com o token
client.run('ODQwMDU1MDk1OTcwMjM0Mzk5.YJSoRg.Pr6dv_758lzs9s-INR6oeOAFGV0')