import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True
token = 'MTAxMjUyNzUzNTk0ODU3MDc1NA.Gzq5Dm.5BOdNlPwbQSNyD6AvknMRC_fjdvjp-FCVgOHd0'


client = MyClient(intents=intents)
client.run(token)