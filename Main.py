import Event from Event
import SongRequest from SongRequest

import discord
import asyncio
import youtube_dl
import sys
import.re

class DiscordBot(discord.Client):

    def __init__(self):
        super().__init__()
        self.queue = asyncio.Queue()

    @asyncio.coroutine
    def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    @asyncio.coroutine
    def on_message(self,message):
        if message.content.startswith('!'):
            messageSplit = re.split(" ",message.content)
            if messageSplit[0] == '!test':
                counter = 0
                tmp = await self.send_message(message.channel, 'Calculating messages...')
                async for log in self.logs_from(message.channel, limit=100):
                    if log.author == message.author:
                        counter += 1

                await self.edit_message(tmp, 'You have {} messages.'.format(counter))
            elif messageSplit[0] == '!sleep':
                await asyncio.sleep(5)
                await self.send_message(message.channel, 'Done sleeping')
            elif messageSplit[0] == '!play':
                if messageSplit[1] == 'queue':
                    #Play queue
                    pass
                elif messageSplit[1] == 'remove':
                    #Play remove 'queue index'
                    pass
                else:
                    #Play 'url'
                    pass

                pass
            elif messageSplit[0] == '!event': #Events
                if messageSplit[1] == 'cancel':
                    #Event cancel 'id'
                    pass
                elif messageSplit[1] == 'set':
                    #Event set 'Title' 'Time' 'Date'
                    pass
                else:
                    #Event
                    pass
                pass


if __name__ = '__main__':
    bot = DiscordBot()
    bot.run(sys.argv[1])
