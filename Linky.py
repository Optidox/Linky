import discord
import os
from dotenv import load_dotenv
from itertools import repeat

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
client = discord.Client()


class Linky(discord.Client):
    async def on_ready(self):
        print(f'Logged in as:\n{self.user.name}\n{self.user.id}\n------')
        await self.change_presence(activity=discord.Game(name='https://github.com/Optidox/Linky'))

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        message_text = message.content
        for _ in repeat(None, message_text.count('https://')):
            links_channel = discord.utils.get(message.guild.channels, name='links')

            if links_channel is None:
                await message.guild.owner.send(f'Link archiving failed at {message.created_at}. Please create a '
                                               f'channel named "links" (case-sensitive) for link archiving.')
                return

            link_index = message_text.find('https://')
            link_end_index = message_text.find(' ', link_index)
            link = message_text[link_index:(link_end_index if link_end_index != -1 else None)]

            await links_channel.send(f'Link sent by {message.author.display_name} on '
                                     f'{message.created_at.strftime("%Y-%m-%d")} at '
                                     f'{message.created_at.strftime("%H:%M:%S")} UTC in <#{message.channel.id}>'
                                     f'\n{link}')
            message_text = message_text[link_end_index:]


load_dotenv()
token = os.getenv('DISCORD_TOKEN')
client = Linky()
client.run(token)
