#!/usr/bin/python3

# import Event from Event
# import SongRequest from SongRequest

import discord
import asyncio
import youtube_dl
import sys
import re


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

    @discord.coroutine
    def on_message(self, message):
        if message.content.startswith('!'):
            messageSplit = re.split(" ", message.content)
            if messageSplit[0] == '!test':
                counter = 0
                tmp = await self.send_message(message.channel, 'Calculating messages...')
                async for log in self.logs_from(message.channel, limit=100):
                    if log.author == message.author:
                        counter += 1

                await self.edit_message(
                    tmp, 'You have {} messages.'.format(counter)
                )
            elif messageSplit[0] == '!sleep':
                await asyncio.sleep(5)
                await self.send_message(message.channel, 'Done Sleeping')
            elif messageSplit[0] == '!play':
                if messageSplit[1] == 'queue':
                    # Play queue
                    await self.send_message(message.channel, 'Added to Queue')
                    pass
                elif messageSplit[1] == 'remove':
                    # Play remove 'queue index'
                    await self.send_message(message.channel,
                                            'Removed from Queue')
                    pass
                else:
                    # Play 'url'
                    await self.send_message(message.channel, 'Playing')
                    pass

                pass
            elif messageSplit[0] == '!event':  # Events
                if messageSplit[1] == 'cancel':
                    # Event cancel 'id'
                    await self.send_message(message.channel, 'Cancelled Event')
                    pass
                elif messageSplit[1] == 'set':
                    # Event set 'Title' 'Time' 'Date'
                    await self.send_message(message.channel, 'New Event')
                    pass
                else:
                    # Event
                    await self.send_message(message.channel, 'Current Event')
                    pass
                pass


if __name__ = '__main__':
    bot = DiscordBot()
    bot.run(sys.argv[1])
