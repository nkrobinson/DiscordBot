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

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        if message.content[0] == "!":
            messageSplit = re.split(" ", message.content)
            if messageSplit[0].lower() == '!test':
                await self.send_message(message.channel, 'Test reply')
            elif messageSplit[0].lower() == '!count':
                counter = 0
                tmp = await self.send_message(message.channel, 'Calculating messages...')
                async for log in self.logs_from(message.channel, limit=100):
                    if log.author == message.author:
                        counter += 1

                await self.edit_message(
                    tmp, 'You have {} messages.'.format(counter)
                )
            elif messageSplit[0].lower() == '!sleep':
                await asyncio.sleep(5)
                await self.send_message(message.channel, 'Done Sleeping')
            elif messageSplit[0].lower() == '!play':
                try:
                    if messageSplit[1] == 'remove':
                        # Play remove 'queue index'
                        await self.send_message(message.channel, 'Removed from Queue')
                    else:
                        url = messageSplit[1]
                        await self.send_message(message.channel, 'Got URL')
                        # if not check(url):
                        #     await self.send_message(message.channel, 'URL not valid')
                        try:
                            self.voice = await self.join_voice_channel(message.author.voice.voice_channel)
                        except:
                            self.voice.move_to(message.author.voice.voice_channel)
                        await self.send_message(message.channel, 'Created Voice')
                        player = await self.voice.create_ytdl_player(url)
                        await self.send_message(message.channel, 'Created Player')
                        player.start()
                        await self.send_message(message.channel, 'Playing')
                except IndexError:
                    # Play 'url'
                    await self.send_message(message.channel, 'Playing')
            elif messageSplit[0].lower() == '!event':  # Events
                try:
                    if messageSplit[1] == 'cancel':
                        # Event cancel 'id'
                        await self.send_message(message.channel, 'Cancelled Event')
                    elif messageSplit[1] == 'set':
                        # Event set 'Title' 'Time' 'Date'
                        await self.send_message(message.channel, 'New Event')
                except:
                    # Current Event
                    await self.send_message(message.channel, 'Current Event')


if __name__ == '__main__':
    bot = DiscordBot()
    bot.run(sys.argv[1])
