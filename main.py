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
        returning_string += ":o:"
    for i in range(array[1]):
        returning_string += ":x:"
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
            try:
                roll_result = Dice.roll(int(message.content[2:]))
                await message.channel.send(roll_format(roll_result))
                await message.channel.send("{0} sucesses".format(str(roll_result[0])))
            except:
                await message.channel.send("uh oh something broke")

# ---- Start the discord client
client = MyClient()
client.run(token[0])

