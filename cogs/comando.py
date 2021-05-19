import discord
from discord.ext import commands
from models.streamer import Streamer
from models.streamerDAO import StreamerDAO 
import sqlite3

msg_id = None
msg_user = None

database = 'database/projectze.db'
conect = sqlite3.connect(database)

#variaveis úteis
# VAR = [PONTOS, CUSTO] obs: de acordo com a loja.
energetico = [20, 50]
coca = [30, 70]
mac = [25, 60]
c_bar = [5, 750]
c_red = [10, 1250]
c_kami = [15, 1500]

class Comando(commands.Cog):
    def __init__(self, client):
        self.client = client

    # cooldown para usar o comando (1,5 sec).
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    
    #<iniciar
    async def iniciar(self, ctx):
        help_embed = discord.Embed(
        title= 'Bem vindo ao José bot! O bot que simula a vida de um streamer!',
        color=3787471,
        description="Para registrar-se digite - <register \n"
                    '\n'
                    "Para ir para a loja digite - <store\n"
                    '\n'                    
                    "Para ver seus status digite - <status\n"
                    '\n'
                    "Para começar uma stream digite- <stream\n"
        )
        #definindo a imagem do embed help
        help_embed.set_image(url='https://imgur.com/ELbZ9aM.png')
        await ctx.send(embed=help_embed)


    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()   
   #<register
    async def register(self, ctx):
        #conectando a dao ao banco de dados
        streamerDAO=StreamerDAO(conect)

        #pegando os atributos do discord de id e nome
        idstreamer = int(ctx.author.id)
        namestreamer = str(ctx.author)

        #criando o personagem inicial com os atributos iniciais
        streamer=Streamer(
            idstreamer,
            namestreamer,
            0,
            50,
            0,
            1000
            ) 
        streamerDAO.cadastro(streamer)

        #conferindo o cadastro
        if streamer.id != None:
            await ctx.send("Cadastrado com sucesso!")
        else:
            await ctx.send('Falha no cadastro.')
            
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()  
    #<loja
    async def loja(self, ctx):
        #criando o embed da loja (Alguns itens vão ser adicionados/mudados )
        loja_embed = discord.Embed(
        title= 'LOJA DE PC',
        color=3787471,
        description="Confira os produtos disponíveis:"
        )
        loja_embed.add_field(name="Energetico", value="50R$", inline=True)
        loja_embed.add_field(name="Coca-Cola", value="70R$", inline=True)
        loja_embed.add_field(name="BigMac", value="60R$", inline=True)
        loja_embed.add_field(name="Cadeira Gamer do bar", value="750R$", inline=True)
        loja_embed.add_field(name="Cadeira Gamer RedDragon", value="1250R$", inline=True)
        loja_embed.add_field(name="Cadeira Gamer do kami", value="1500R$", inline=True)
        loja_embed.add_field(name="Intel I3", value="750R$", inline=True)
        loja_embed.add_field(name="Intel I5", value="2000R$", inline=True)
        loja_embed.add_field(name="Intel I7", value="3500R$", inline=True)
        loja_embed.add_field(name="GeForce 1080", value="5000R$", inline=True)
        loja_embed.add_field(name="GeForce 2060", value="4500R$", inline=True)
        loja_embed.add_field(name="GeForce 2070", value="5500R$", inline=True)

        loja_embed.set_footer(text="Escolha 1 dos itens acima digitando: <buy item_name")
        await ctx.send(embed=loja_embed)

    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()  
    #<buy
    async def buy(self, ctx):
        user = StreamerDAO(conect)
        info = StreamerDAO(conect)
        info = info.pesquisar(iduser)
        mensagem = str(ctx.message.content)
        mensagem = mensagem.replace("<buy ","")
        if mensagem.upper() == "ENERGETICO":
            user.atualiza_stamina(int(ctx.author.id), int(info[0][3]) + int(energetico[0]))
            user.atualiza_dinheiro(int(ctx.author.id), int(info[0][5]) - int(energetico[1]))
            await ctx.send(f'{ctx.author.mention} acabou de pagar {str(energetico[1])}R$ e comprou um {mensagem.replace("item:","").capitalize()}, ganhando mais {str(energetico[0])} de stamina para streamar!')
        elif mensagem.upper() == "COCA-COLA":
            user.atualiza_stamina(int(ctx.author.id), int(info[0][3]) + int(coca[0]))
            user.atualiza_dinheiro(int(ctx.author.id), int(info[0][5]) - int(coca[1]))
            await ctx.send(f'{ctx.author.mention} acabou de pagar {str(coca[1])}R$ e comprou uma {mensagem.replace("item:","").capitalize()}, ganhando mais {str(coca[0])} de stamina para streamar!')
        elif mensagem.upper() == "BIGMAC":
            user.atualiza_stamina(int(ctx.author.id), int(info[0][3]) + int(mac[0]))
            user.atualiza_dinheiro(int(ctx.author.id), int(info[0][5]) - int(mac[1]))
            await ctx.send(f'{ctx.author.mention} acabou de pagar {str(mac[1])}R$ e comprou um {mensagem.replace("item:","").capitalize()}, ganhando mais {str(mac[0])} de stamina para streamar!')
        elif mensagem.upper() == "CADEIRA GAMER DO BAR":
            user.atualiza_stamina(int(ctx.author.id), int(info[0][3]) + int(c_bar[0]))
            user.atualiza_dinheiro(int(ctx.author.id), int(info[0][5]) - int(c_bar[1]))
            await ctx.send(f'{ctx.author.mention} acabou de pagar {str(c_bar[1])}R$ e comprou uma {mensagem.replace("item:","").capitalize()}, dessa forma, gastando {str(c_bar[0])} pontos(s) a menos de stamina durante 1 hora de live!')
        elif mensagem.upper() == "CADEIRA GAMER REDDRAGON":
            user.atualiza_stamina(int(ctx.author.id), int(info[0][3]) + int(c_red[0]))
            user.atualiza_dinheiro(int(ctx.author.id), int(info[0][5]) - int(c_red[1]))
            await ctx.send(f'{ctx.author.mention} acabou de pagar {str(c_red[1])}R$ e comprou uma {mensagem.replace("item:","").capitalize()}, dessa forma, gastando {str(c_red[0])} pontos(s) a menos de stamina durante 1 hora de live!')
        elif mensagem.upper() == "CADEIRA GAMER DO KAMI":
            user.atualiza_stamina(int(ctx.author.id), int(info[0][3]) + int(c_kami[0]))
            user.atualiza_dinheiro(int(ctx.author.id), int(info[0][5]) - int(c_kami[1]))
            await ctx.send(f'{ctx.author.mention} acabou de pagar {str(c_kami[1])}R$ e comprou uma {mensagem.replace("item:","").capitalize()}, dessa forma, gastando {str(c_kami[0])} pontos(s) a menos de stamina durante 1 hora de live!')
        else:
            await ctx.send(f'{ctx.author.mention}, o item que você solicitou não está em nosso catalogo. Por favor, tente novamente!')

    #<info
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command() 
    async def info(self, ctx):
        iduser = int(ctx.author.id)
        info = StreamerDAO(conect)
        info = info.pesquisar(iduser)
        embed=discord.Embed(title="Informações do usuario", color=0x00fbff)
        embed.add_field(name="Nome", value=info[0][1], inline=True)
        embed.add_field(name="Level", value=info[0][2], inline=True)
        embed.add_field(name="Stamina", value=info[0][3], inline=True) 
        embed.add_field(name="Subs", value=info[0][4], inline=True)
        embed.add_field(name="Dinheiro", value=info[0][5], inline=True)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Comando(client))