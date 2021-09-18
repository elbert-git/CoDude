from modules import Dice
import discord
import asyncio
import random

#get token id
token_file = open('token.env', 'r')
token = token_file.readlines()
token_file.close()
print(token)

# ---- Discord client setup
#this func just returns Xs and Os based on array
def roll_format(array):
    returning_string = ""
    for i in range(array[0]):
        returning_string += "O"
    for i in range(array[1]):
        returning_string += "X"
    return returning_string

# ---- Discord client setup
class MyClient(discord.Client):
    async def on_ready(self):
        print('logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content == "!Rdestiny":
            await message.channel.send(random.randrange(1,21))
            return

        if message.content.startswith('!R'):
            await message.channel.send(roll_format(Dice.roll(int(message.content[2:]))))

# ---- Start the discord client
client = MyClient()
client.run(token[0])

