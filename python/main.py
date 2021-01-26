import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author} - {0.channel}: {0.content}'.format(message))
        if message.author == client.user:
            return

        if message.content.startswith('hello'):
            await message.channel.send('Hello~')

client = MyClient()

client.run('')

