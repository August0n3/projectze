import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!dark'):
        await message.channel.send('O maior lixo do server')

    if message.content.startswith('!nishida'):
        await message.channel.send('fofinho :3')

client.run('ODQwMDU1MDk1OTcwMjM0Mzk5.YJSoRg.Pr6dv_758lzs9s-INR6oeOAFGV0')