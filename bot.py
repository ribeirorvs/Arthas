import discord

intents = discord.Intents.default()
intents.message_content = True
token = ''

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    global guilds, mutados, deitados
    print(f'We have logged in as {client.user}')
    guilds = discord.utils.get(client.guilds)
    mutados = discord.utils.get(guilds.channels, name='Mutados')
    deitados = discord.utils.get(guilds.channels, name='Trabalhando deitado')
    for channel in guilds.channels:
        if channel.name != 'general' or channel.name != 'Mutados':
            for user in channel.members:
                if user != client.user:
                    voice = user.voice
                    if voice.self_mute or voice.self_deaf:
                        await user.move_to(mutados)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

def check_channels():
    for channel in guilds.channels:
            if channel.name == 'general' or channel.name == 'Mutados':
                continue
            else:
                if len(channel.members) > 0:
                    return channel
    return deitados

@client.event
async def on_voice_state_update(member, before, after):
    if after.self_deaf or after.self_mute:
        if member.voice.channel.name != 'Mutados':
            await member.move_to(mutados)
    elif not after.self_deaf and not after.self_mute:
        if member.voice.channel.name == 'Mutados':
            await member.move_to(check_channels())

client.run(token)