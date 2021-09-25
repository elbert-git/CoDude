from modules import Dice
import discord
import asyncio
import random

#get token id
token_file = open('token.env', 'r')
token = token_file.readlines()
token_file.close()
print(token)


# handle character data



# ---- functions

#this func just returns Xs and Os based on array (in emotes)
def roll_format(array):
    returning_string = ""
    for i in range(array[0]):
        returning_string += ":o:"
    for i in range(array[1]):
        returning_string += ":x:"
    return returning_string

#this func handles rolling input and return final string to send to discord
def rolling_input(message_string, user_name):
    #parse message input
    split_input_string = message_string.split(' ')
    is_attribute_roll = false #just to initialise this integer
    #check if attribute roll just integer roll
    try:
        test = int(split_input_string[-1])
        is_attribute_roll = false
    except:
        is_attribute_roll = true
    #if attribute roll
    if is_attribute_roll:
        pass
        #get apprioriate json
        #get raw dice count
        #add root attribute dice
        #add base dice
        #set roll_array


    #if just simple integer roll
    else:
        roll_array = Dice.roll(int(split_input_string[:-1]))

    #get returning string
    returning_string = roll_format(roll_array)
    

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

        #this handles rolling input
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

